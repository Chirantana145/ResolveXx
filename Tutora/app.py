from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import google.generativeai as genai
import PyPDF2
import json
import uuid
from datetime import datetime
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# MySQL Database Configuration
DB_CONFIG = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE', 'tutora_ai'),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}

# Configure Gemini AI
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-2.5-flash') 
# 'gemini-1.5-pro-latest' is a better alternative for text generation.

# Database Helper Functions
def get_db_connection():
    """Create and return MySQL connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def close_db_connection(connection, cursor):
    """Close MySQL connection and cursor"""
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()

# File Processing Functions
def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return ""

# API Routes
@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_from_directory('.', 'index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle file upload and text extraction"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    file_type = file.content_type
    
    # Extract text based on file type
    if file_type == 'application/pdf':
        text = extract_text_from_pdf(file)
    elif file_type == 'text/plain':
        text = file.read().decode('utf-8')
    else:
        return jsonify({'error': 'Unsupported file type'}), 400
    
    return jsonify({
        'success': True,
        'filename': file.filename,
        'text': text[:500],  # Return first 500 chars for preview
        'full_text': text
    })

@app.route('/api/generate-quiz', methods=['POST'])
def generate_quiz():
    """Generate quiz from study material using AI"""
    data = request.json
    study_material = data.get('text', '')
    num_questions = data.get('num_questions', 5)
    difficulty = data.get('difficulty', 'medium')
    
    prompt = f"""You are an expert educator. Generate {num_questions} multiple choice questions from the following study material.

Difficulty Level: {difficulty}

Study Material:
{study_material}

Return ONLY valid JSON in this exact format:
{{
  "questions": [
    {{
      "question": "Question text here?",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "correct_answer": 0,
      "explanation": "Why this is correct"
    }}
  ]
}}"""
    
    try:
        response = model.generate_content(prompt)
        # Extract JSON from response
        result_text = response.text.strip()
        if result_text.startswith('```json'):
            result_text = result_text[7:-3]
        elif result_text.startswith('```'):
            result_text = result_text[3:-3]
        
        quiz_data = json.loads(result_text)
        return jsonify(quiz_data)
    
    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        print(f"Raw Gemini response: {response.text}")
        return jsonify({'error': 'AI failed to generate valid quiz data. Please try again with different content.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat_with_tutor():
    """Chat with AI tutor about study materials"""
    data = request.json
    user_message = data.get('message', '')
    study_context = data.get('context', '')
    
    # Build conversation context
    system_prompt = f"""You are a helpful and patient AI tutor. Answer student questions based on their study materials.
    
Study Material Context:
{study_context}

Be encouraging, clear, and provide examples when helpful."""
    
    try:
        full_prompt = f"{system_prompt}\n\nStudent Question: {user_message}\n\nAnswer:"
        response = model.generate_content(full_prompt)
        
        return jsonify({
            'response': response.text,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/save-material', methods=['POST'])
def save_material():
    """Save study material to database"""
    data = request.json
    connection = get_db_connection()
    
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        material_id = str(uuid.uuid4())
        
        query = """
            INSERT INTO study_materials (id, user_id, filename, file_type, content_text)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (
            material_id,
            data['user_id'],
            data['filename'],
            data['file_type'],
            data['content']
        )
        
        cursor.execute(query, values)
        connection.commit()
        
        return jsonify({
            'success': True,
            'id': material_id,
            'message': 'Material saved successfully'
        })
    
    except Error as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        close_db_connection(connection, cursor)

@app.route('/api/save-quiz-attempt', methods=['POST'])
def save_quiz_attempt():
    """Save quiz attempt results"""
    data = request.json
    connection = get_db_connection()
    
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        attempt_id = str(uuid.uuid4())
        
        query = """
            INSERT INTO quiz_attempts (id, user_id, quiz_id, score, total_questions, answers)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            attempt_id,
            data['user_id'],
            data['quiz_id'],
            data['score'],
            data['total_questions'],
            json.dumps(data['answers'])  # Convert to JSON string
        )
        
        cursor.execute(query, values)
        connection.commit()
        
        return jsonify({
            'success': True,
            'id': attempt_id,
            'message': 'Quiz attempt saved successfully'
        })
    
    except Error as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        close_db_connection(connection, cursor)

@app.route('/api/get-progress/<user_id>', methods=['GET'])
def get_progress(user_id):
    """Get user's learning progress"""
    connection = get_db_connection()
    
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # Get quiz attempts
        cursor.execute("""
            SELECT * FROM quiz_attempts 
            WHERE user_id = %s 
            ORDER BY completed_at DESC
        """, (user_id,))
        attempts = cursor.fetchall()
        
        # Convert JSON strings back to objects
        for attempt in attempts:
            if attempt['answers']:
                attempt['answers'] = json.loads(attempt['answers'])
        
        # Get study materials
        cursor.execute("""
            SELECT * FROM study_materials 
            WHERE user_id = %s 
            ORDER BY upload_date DESC
        """, (user_id,))
        materials = cursor.fetchall()
        
        return jsonify({
            'attempts': attempts,
            'materials': materials
        })
    
    except Error as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        close_db_connection(connection, cursor)

@app.route('/api/materials/<user_id>', methods=['GET'])
def get_materials(user_id):
    """Get all materials for a user"""
    connection = get_db_connection()
    
    if not connection:
        return jsonify({'error': 'Database connection failed'}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT id, filename, file_type, upload_date 
            FROM study_materials 
            WHERE user_id = %s 
            ORDER BY upload_date DESC
        """, (user_id,))
        
        materials = cursor.fetchall()
        return jsonify({'materials': materials})
    
    except Error as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        close_db_connection(connection, cursor)

@app.route('/api/test-connection', methods=['GET'])
def test_connection():
    """Test database connection"""
    connection = get_db_connection()
    
    if connection and connection.is_connected():
        db_info = connection.get_server_info()
        connection.close()
        return jsonify({
            'success': True,
            'message': 'Successfully connected to MySQL',
            'version': db_info
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Failed to connect to MySQL'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """API health check"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("Starting TUTORA AI Backend Server...")
    print(f"Database: {DB_CONFIG['database']} on {DB_CONFIG['host']}")
    app.run(debug=True, port=5000)
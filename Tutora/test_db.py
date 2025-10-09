import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

try:
    connection = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DATABASE')
    )
    
    if connection.is_connected():
        print("✓ Successfully connected to MySQL")
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        print(f"✓ Found {len(tables)} tables in database")
        for table in tables:
            print(f"  - {table[0]}")
        cursor.close()
        connection.close()
except Exception as e:
    print(f"✗ Error: {e}")
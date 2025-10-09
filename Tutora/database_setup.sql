-- Create Database
CREATE DATABASE IF NOT EXISTS tutora_ai;
USE tutora_ai;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    password_hash VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Study materials table
CREATE TABLE IF NOT EXISTS study_materials (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36),
    filename VARCHAR(255),
    file_type VARCHAR(50),
    content_text LONGTEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Quizzes table
CREATE TABLE IF NOT EXISTS quizzes (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36),
    material_id VARCHAR(36),
    questions JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES study_materials(id) ON DELETE CASCADE
);

-- Quiz attempts table
CREATE TABLE IF NOT EXISTS quiz_attempts (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36),
    quiz_id VARCHAR(36),
    score INTEGER,
    total_questions INTEGER,
    answers JSON,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
);

-- Chat history table
CREATE TABLE IF NOT EXISTS chat_history (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36),
    message TEXT,
    sender VARCHAR(20),
    material_id VARCHAR(36),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES study_materials(id) ON DELETE SET NULL
);

-- User progress table
CREATE TABLE IF NOT EXISTS user_progress (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36),
    total_quizzes INTEGER DEFAULT 0,
    total_score FLOAT DEFAULT 0,
    average_score FLOAT DEFAULT 0,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
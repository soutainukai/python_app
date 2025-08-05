import sqlite3

def init_db():
    conn = sqlite3.connect("inquiries.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT,
            response TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(name,email,message,response):
    conn = sqlite3.connect("inquiries.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contact (name,email,message,response)
        VALUES (?,?,?, ?)
    """, (name,email,message,response))
    conn.commit()
    conn.close()
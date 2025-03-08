import sqlite3
from core.config import DATABASE_URL

def get_connection():
    conn = sqlite3.connect(DATABASE_URL)
    return conn

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS egg_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            eggs_detected INTEGER,
            detections TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_result(eggs_detected: int, detections: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO egg_results (eggs_detected, detections) VALUES (?, ?)", (eggs_detected, detections))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Base de datos inicializada correctamente.")

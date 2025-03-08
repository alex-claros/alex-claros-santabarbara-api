import sqlite3
from core.config import DATABASE_URL

def get_connection():
    return sqlite3.connect(DATABASE_URL)

def initialize_incubator_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incubators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            temperature REAL NOT NULL,
            humidity REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def create_incubator(location: str, capacity: int, temperature: float, humidity: float) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO incubators (location, capacity, temperature, humidity)
        VALUES (?, ?, ?, ?)
    """, (location, capacity, temperature, humidity))
    conn.commit()
    incubator_id = cursor.lastrowid
    conn.close()
    return incubator_id

def get_incubator_by_id(incubator_id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, location, capacity, temperature, humidity FROM incubators WHERE id = ?", (incubator_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "location": row[1],
            "capacity": row[2],
            "temperature": row[3],
            "humidity": row[4]
        }
    return None

def get_all_incubators() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, location, capacity, temperature, humidity FROM incubators")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "location": row[1],
            "capacity": row[2],
            "temperature": row[3],
            "humidity": row[4]
        } for row in rows
    ]

def update_incubator(incubator_id: int, location: str, capacity: int, temperature: float, humidity: float) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE incubators 
        SET location = ?, capacity = ?, temperature = ?, humidity = ?
        WHERE id = ?
    """, (location, capacity, temperature, humidity, incubator_id))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def delete_incubator(incubator_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM incubators WHERE id = ?", (incubator_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

if __name__ == "__main__":
    initialize_incubator_table()
    print("Tabla de incubadoras inicializada correctamente.")

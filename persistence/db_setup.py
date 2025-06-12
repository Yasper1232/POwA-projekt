import sqlite3

def initialize_database():
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()

    # Tabela klientów
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            pesel TEXT UNIQUE NOT NULL,
            address TEXT
        )
    ''')

    # Tabela leków
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dosage TEXT,
            quantity INTEGER,
            expiry_date TEXT
        )
    ''')

    conn.commit()
    conn.close()

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

#tabela wiele do wielu :::
    cursor.execute('''CREATE TABLE IF NOT EXISTS assigned_medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    medicine_id INTEGER NOT NULL,
    assigned_date TEXT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (medicine_id) REFERENCES medicines(id)
)''')



    conn.commit()
    conn.close()

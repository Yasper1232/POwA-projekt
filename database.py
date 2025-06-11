import sqlite3

# Połącz z bazą danych (plik .db zostanie utworzony automatycznie)
conn = sqlite3.connect('pharmacy.db')
cursor = conn.cursor()

# Utwórz tabelę klientów
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        pesel TEXT UNIQUE NOT NULL,
        address TEXT
    )
''')

# Utwórz tabelę leków
cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        dosage TEXT,
        quantity INTEGER,
        expiry_date TEXT
    )
''')

# Zapisz zmiany i zamknij połączenie
conn.commit()
conn.close()

print("Baza danych i tabele zostały utworzone.")

import sqlite3

def add_client(first_name, last_name, pesel, address):
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO clients (first_name, last_name, pesel, address)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, pesel, address))
        conn.commit()
        print("✅ Klient dodany pomyślnie.")
    except sqlite3.IntegrityError:
        print("❌ Klient z takim PESEL-em już istnieje.")
    finally:
        conn.close()

# Możemy dodać też np. funkcję pobierającą klientów
def get_clients():
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    rows = cursor.fetchall()
    conn.close()
    return rows

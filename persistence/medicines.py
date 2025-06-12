import sqlite3

def add_medicine(name, dosage, quantity, expiry_date):
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO medicines (name, dosage, quantity, expiry_date)
        VALUES (?, ?, ?, ?)
    ''', (name, dosage, quantity, expiry_date))

    conn.commit()
    conn.close()
    print("✅ Lek dodany pomyślnie.")

def get_medicines():
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM medicines')
    rows = cursor.fetchall()
    conn.close()
    return rows

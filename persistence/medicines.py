from models.medicine import Medicine
from datetime import datetime
import sqlite3

def add_medicine(medicine: Medicine):
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO medicines (name, dosage, quantity, expiry_date)
        VALUES (?, ?, ?, ?)
    ''', (medicine.name,
          medicine.dosage, medicine.quantity,
          medicine.expiry_date.strftime("%Y-%m-%d")))
#konwertujemy expiry_date na string , bo sqllite tego wymaga
    conn.commit()
    conn.close()
    print("✅ Lek dodany pomyślnie.")
#funkcja w argumencie przyjmuje obiekt typu Medicine ,
# z tego obiektu pobiera pola ktore zapisuje do bazy
#gdy chce dodac nowy lek ,to tworze obiekt typu Medicine : nowy_lek = Medicine(id=0, name="Paracetamol", dosage="500mg", quantity=50, expiry_date=date(2026, 5, 20))
# nastepnie bede wywolywal : add_medicine(nowy_lek)

def get_medicines():
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, dosage, quantity, expiry_date FROM medicines')
    rows = cursor.fetchall()
    conn.close()

    medicines = []
    for row in rows:
        id_, name, dosage, quantity, expiry_str = row
        expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d").date()
        medicines.append(Medicine(id=id_, name=name, dosage=dosage, quantity=quantity, expiry_date=expiry_date))

    return medicines

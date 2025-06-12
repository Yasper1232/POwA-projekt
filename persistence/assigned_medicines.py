import sqlite3
from models.assigned_medicine import AssignedMedicine
import sqlite3
from models.medicine import Medicine
from datetime import datetime

def assign_medicine(assignment: AssignedMedicine):
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO assigned_medicines (client_id, medicine_id, assigned_date)
        VALUES (?, ?, ?)
    """, (assignment.client_id, assignment.medicine_id, assignment.assigned_date.isoformat()))
    conn.commit()
    conn.close()


def get_medicines_for_client(client_id: int):
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT m.id, m.name, m.dosage, m.quantity, m.expiry_date, a.assigned_date
        FROM medicines m
        JOIN assigned_medicines a ON m.id = a.medicine_id
        WHERE a.client_id = ?
    """, (client_id,))

    rows = cursor.fetchall()
    conn.close()

    medicines = [{
        "medicine": Medicine(
            id=row[0],
            name=row[1],
            dosage=row[2],
            quantity=row[3],
            expiry_date=row[4]
        ),
        "assigned_date": row[5]
    } for row in rows]

    return medicines
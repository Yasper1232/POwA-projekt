import sqlite3

from models.client import Client

def add_client(client: Client):
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clients (first_name, last_name, pesel, address) VALUES (?, ?, ?, ?)",
        (client.first_name, client.last_name, client.pesel, client.address)
    )
    conn.commit()
    conn.close()

def get_clients():
    conn = sqlite3.connect('pharmacy.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, pesel, address FROM clients")
    rows = cursor.fetchall()
    conn.close()

    clients = [Client(id=row[0], first_name=row[1], last_name=row[2], pesel=row[3], address=row[4]) for row in rows]
    return clients
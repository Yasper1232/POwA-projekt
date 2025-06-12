from models.client import Client
from models.medicine import Medicine
from persistence.clients import add_client as add_client_db, get_clients as get_clients_db
from persistence.medicines import add_medicine as add_medicine_db, get_medicines as get_medicines_db
from datetime import datetime

def main_menu():
    while True:
        print("\n=== PharmaManager ===")
        print("1. Manage Clients")
        print("2. Manage Medicines")
        print("3. Assign Medicines to Clients")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            client_menu()
        elif choice == '2':
            medicine_menu()
        elif choice == '3':
            assign_medicines()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# ------- CLIENTS ---------

def client_menu():
    while True:
        print("\n--- Client Management ---")
        print("1. Add Client")
        print("2. Get All Clients")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_client()
        elif choice == '2':
            get_clients()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

def add_client():
    first = input("First name: ")
    last = input("Last name: ")
    pesel = input("PESEL: ")
    addr = input("Address: ")
    client = Client(id=0, first_name=first, last_name=last, pesel=pesel, address=addr)
    add_client_db(client)  # zmień import z persistance na add_client_db, żeby uniknąć kolizji nazw

def get_clients():
    clients = get_clients_db()
    print("\n--- Clients List ---")
    for c in clients:
        print(f"{c.id}. {c.first_name} {c.last_name} | PESEL: {c.pesel} | Address: {c.address}")

# ------- MEDICINES ---------

def medicine_menu():
    while True:
        print("\n--- Medicine Management ---")
        print("1. Add Medicine")
        print("2. View All Medicines")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_medicine()
        elif choice == '2':
            get_medicines()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

def medicine_menu():
    while True:
        print("\n--- Medicine Management ---")
        print("1. Add Medicine")
        print("2. Get All Medicines")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_medicine()
        elif choice == '2':
            get_medicines()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

def add_medicine():
    name = input("Medicine name: ")
    dosage = input("Dosage (e.g. 500mg): ")
    quantity = int(input("Quantity: "))
    expiry_str = input("Expiry date (YYYY-MM-DD): ")

    try:
        expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d").date()
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")
        return

    medicine = Medicine(id=0, name=name, dosage=dosage, quantity=quantity, expiry_date=expiry_date)
    add_medicine_db(medicine)

def get_medicines():
    medicines = get_medicines_db()
    print("\n--- Medicines List ---")
    for m in medicines:
        print(f"{m.id}. {m.name} | {m.dosage} | Qty: {m.quantity} | Exp: {m.expiry_date}")

# ------- FUTURE FEATURE ---------

def assign_medicines():
    print("Feature coming soon...")

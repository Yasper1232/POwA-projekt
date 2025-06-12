from models.client import Client
from persistence.clients import add_client as add_client_db, get_clients as get_clients_db
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

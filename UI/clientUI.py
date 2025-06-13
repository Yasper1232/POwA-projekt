from UI.assignmedicineUI import view_medicines_for_client
from models.client import Client
from persistence.clients import update_client, client_exists
from persistence.clients import delete_client as delete_client_db

from persistence.clients import add_client as add_client_db, get_clients as get_clients_db
def client_menu():
    while True:
        print("\n--- Client Management ---")
        print("1. Add Client")
        print("2. Get All Clients")
        print("3. Edit Client")
        print("4. Delete Client")
        print("5. View Medicine for Client")
        print("6. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_client()
        elif choice == '2':
            get_clients()
        elif choice == '3':
            edit_client()
        elif choice == '4':
            delete_client()
        elif choice == '5':
            view_medicines_for_client()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Try again.")

from models.client import Client
from persistence.clients import add_client as add_client_db, client_exists

def add_client():
    first = input("First name: ")
    last = input("Last name: ")
    pesel = input("PESEL: ")
    addr = input("Address: ")

    if client_exists(pesel):
        print("Client with this PESEL already exists.")
        return

    client = Client(id=0, first_name=first, last_name=last, pesel=pesel, address=addr)
    add_client_db(client)
    print("✅ Client added successfully.")


def get_clients():
    clients = get_clients_db()
    print("\n--- Clients List ---")
    for c in clients:
        print(f"{c.id}. {c.first_name} {c.last_name} | PESEL: {c.pesel} | Address: {c.address}")


def edit_client():
    clients = get_clients_db()
    if not clients:
        print("No clients found.")
        return

    print("\n--- Edit Client ---")
    for c in clients:
        print(f"{c.id}. {c.first_name} {c.last_name} | PESEL: {c.pesel} | Address: {c.address}")

    try:
        client_id = int(input("Enter the ID of the client you want to edit: "))
    except ValueError:
        print("❌ Invalid input. ID must be a number.")
        return

    client_to_edit = next((c for c in clients if c.id == client_id), None)

    if not client_to_edit:
        print("❌ No client found with that ID.")
        return

    print("Leave a field blank to keep the current value.\n")

    first = input(f"First name [{client_to_edit.first_name}]: ") or client_to_edit.first_name
    last = input(f"Last name [{client_to_edit.last_name}]: ") or client_to_edit.last_name
    pesel = input(f"PESEL [{client_to_edit.pesel}]: ") or client_to_edit.pesel
    addr = input(f"Address [{client_to_edit.address}]: ") or client_to_edit.address

    updated_client = Client(
        id=client_to_edit.id,
        first_name=first,
        last_name=last,
        pesel=pesel,
        address=addr
    )

    update_client(updated_client)
    print("✅ Client updated successfully.")


def delete_client():
    try:
        client_id = int(input("Enter the ID of the client to delete: "))
        success = delete_client_db(client_id)
        if success:
            print("✅ Client deleted successfully.")
        else:
            print("❌ No client found with that ID.")
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
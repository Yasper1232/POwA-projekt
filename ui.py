from persistence.db_setup import initialize_database
from persistence.clients import add_client, get_clients
from persistence.medicines import add_medicine, get_medicines


#Przeniosłem logikę ui do osobnego pliku,
#co jest zgodne z zasada Separation of Concerns
#jak i rowniez S z solid, ktora mowi ze klasa,moduł powinien miec jedna odpowiedzialnosc,
# wiec UI tylko w pliku ui.py!!!

def main_menu():
    while True:
        print("\n=== PharmaManager ===")
        print("1. Manage Clients")
        print("2. Manage Medicines")
        print("3. Assign Medicines to Clients")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            manage_clients()
        elif choice == '2':
            manage_medicines()
        elif choice == '3':
            assign_medicines()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_clients():
    print("\n--- Manage Clients ---")
    first = input("First name: ")
    last = input("Last name: ")
    pesel = input("PESEL: ")
    addr = input("Address: ")
    add_client(first, last, pesel, addr)

def manage_medicines():
    print("\n--- Manage Medicines ---")
    name = input("Medicine name: ")
    dosage = input("Dosage (e.g. 500mg): ")
    quantity = int(input("Quantity: "))
    expiry = input("Expiry date (YYYY-MM-DD): ")
    add_medicine(name, dosage, quantity, expiry)

def assign_medicines():
    print("Feature coming soon...")

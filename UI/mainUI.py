from UI.clientUI import client_menu
from UI.medicineUI import medicine_menu
from UI.assignmedicineUI import assign_medicine_to_client

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
            assign_medicine_to_client()

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")





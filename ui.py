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
    print("Manage Clients - feature coming soon...")

def manage_medicines():
    print("Manage Medicines - feature coming soon...")

def assign_medicines():
    print("Assign Medicines - feature coming soon...")

if __name__ == "__main__":
    main_menu()

from models.medicine import Medicine
from persistence.medicines import add_medicine as add_medicine_db, get_medicines as get_medicines_db
from datetime import datetime
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

from models.medicine import Medicine
from persistence.medicines import add_medicine as add_medicine_db, get_medicines as get_medicines_db
from datetime import datetime
from persistence.medicines import get_medicines as get_medicines_db, update_medicine, delete_medicine as delete_medicine_db

def medicine_menu():
    while True:
        print("\n--- Medicine Management ---")
        print("1. Add Medicine")
        print("2. Get All Medicines")
        print("3. Edit Medicine")
        print("4. Delete Medicine")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            add_medicine()
        elif choice == '2':
            get_medicines()
        elif choice == '3':
            edit_medicine()
        elif choice == '4':
            delete_medicine()
        elif choice == '5':
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

def edit_medicine():
    medicines = get_medicines_db()
    if not medicines:
        print("No medicines found.")
        return

    print("\n--- Edit Medicine ---")
    for m in medicines:
        print(f"{m.id}. {m.name} | {m.description} | Qty: {m.quantity} | Price: {m.price}")

    try:
        medicine_id = int(input("Enter the ID of the medicine to edit: "))
    except ValueError:
        print("❌ Invalid input. ID must be a number.")
        return

    medicine_to_edit = next((m for m in medicines if m.id == medicine_id), None)
    if not medicine_to_edit:
        print("❌ No medicine found with that ID.")
        return

    print("Leave a field blank to keep the current value.\n")

    name = input(f"Name [{medicine_to_edit.name}]: ") or medicine_to_edit.name
    desc = input(f"Description [{medicine_to_edit.description}]: ") or medicine_to_edit.description

    try:
        qty_input = input(f"Quantity [{medicine_to_edit.quantity}]: ")
        quantity = int(qty_input) if qty_input else medicine_to_edit.quantity

        price_input = input(f"Price [{medicine_to_edit.price}]: ")
        price = float(price_input) if price_input else medicine_to_edit.price
    except ValueError:
        print("❌ Invalid number format.")
        return

    updated = Medicine(
        id=medicine_to_edit.id,
        name=name,
        description=desc,
        quantity=quantity,
        price=price
    )

    update_medicine(updated)
    print("✅ Medicine updated successfully.")


def delete_medicine():
    try:
        medicine_id = int(input("Enter the ID of the medicine to delete: "))
        success = delete_medicine_db(medicine_id)
        if success:
            print("✅ Medicine deleted successfully.")
        else:
            print("❌ No medicine found with that ID.")
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
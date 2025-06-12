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
        print(f"{m.id}. {m.name} | Dosage: {m.dosage} | Qty: {m.quantity} | Expires: {m.expiry_date}")

    try:
        med_id = int(input("Enter the ID of the medicine you want to edit: "))
    except ValueError:
        print("❌ Invalid input. ID must be a number.")
        return

    medicine_to_edit = next((m for m in medicines if m.id == med_id), None)
    if not medicine_to_edit:
        print("❌ No medicine found with that ID.")
        return

    print("Leave a field blank to keep the current value.\n")

    name = input(f"Name [{medicine_to_edit.name}]: ") or medicine_to_edit.name
    dosage = input(f"Dosage [{medicine_to_edit.dosage}]: ") or medicine_to_edit.dosage
    quantity_input = input(f"Quantity [{medicine_to_edit.quantity}]: ")
    expiry_input = input(f"Expiry Date (YYYY-MM-DD) [{medicine_to_edit.expiry_date}]: ")

    # Parsuj dane wejściowe lub zachowaj stare
    try:
        quantity = int(quantity_input) if quantity_input else medicine_to_edit.quantity
    except ValueError:
        print("❌ Invalid quantity.")
        return

    try:
        expiry_date = datetime.strptime(expiry_input, "%Y-%m-%d").date() if expiry_input else medicine_to_edit.expiry_date
    except ValueError:
        print("❌ Invalid date format.")
        return

    updated_med = Medicine(
        id=medicine_to_edit.id,
        name=name,
        dosage=dosage,
        quantity=quantity,
        expiry_date=expiry_date
    )

    update_medicine(updated_med)
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
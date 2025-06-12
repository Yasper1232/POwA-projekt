from datetime import date
from models.assigned_medicine import AssignedMedicine
from persistence.clients import get_clients as get_clients_db
from persistence.medicines import get_medicines as get_medicines_db
from persistence.assigned_medicines import assign_medicine
from persistence.assigned_medicines import get_medicines_for_client
from persistence.clients import get_clients

def assign_medicine_to_client():
    clients = get_clients_db()
    medicines = get_medicines_db()

    if not clients:
        print("❌ No clients found.")
        return

    if not medicines:
        print("❌ No medicines found.")
        return

    print("\n--- Clients ---")
    for c in clients:
        print(f"{c.id}: {c.first_name} {c.last_name}")

    try:
        client_id = int(input("Enter Client ID: "))
    except ValueError:
        print("❌ Invalid client ID.")
        return

    print("\n--- Medicines ---")
    for m in medicines:
        print(f"{m.id}: {m.name} ({m.dosage})")

    try:
        medicine_id = int(input("Enter Medicine ID: "))
    except ValueError:
        print("❌ Invalid medicine ID.")
        return

    date_str = input("Enter date (YYYY-MM-DD): ")
    try:
        assign_date = date.fromisoformat(date_str)
    except ValueError:
        print("❌ Invalid date format.")
        return

    assignment = AssignedMedicine(
        id=0,
        client_id=client_id,
        medicine_id=medicine_id,
        assigned_date=assign_date
    )

    assign_medicine(assignment)
    print("✅ Medicine assigned to client.")


def view_medicines_for_client():
    clients = get_clients()
    if not clients:
        print("❌ No clients found.")
        return

    print("\n--- Select Client ---")
    for c in clients:
        print(f"{c.id}. {c.first_name} {c.last_name}")

    try:
        client_id = int(input("Enter client ID: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    assigned_medicines = get_medicines_for_client(client_id)

    if not assigned_medicines:
        print("ℹ️ No medicines assigned to this client.")
    else:
        print(f"\n💊 Medicines assigned to client ID {client_id}:")
        for item in assigned_medicines:
            m = item["medicine"]
            print(f"- {m.name} ({m.dosage}) | Qty: {m.quantity} | Expires: {m.expiry_date} | Assigned: {item['assigned_date']}")
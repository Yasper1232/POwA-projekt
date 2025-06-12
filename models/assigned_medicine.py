from dataclasses import dataclass
from datetime import date

@dataclass
class AssignedMedicine:
    id: int
    client_id: int
    medicine_id: int
    assigned_date: date

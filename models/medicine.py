from dataclasses import dataclass
from datetime import date

@dataclass
class Medicine:
    id: int
    name: str
    dosage: str
    quantity: int
    expiry_date: date

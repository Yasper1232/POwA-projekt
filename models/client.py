from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Client:
    first_name: str
    last_name: str
    pesel: str
    address: str
    id: Optional[int] = field(default=None)  # na końcu!

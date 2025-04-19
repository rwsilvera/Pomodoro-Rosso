from dataclasses import dataclass
from typing import Optional

@dataclass
class Producto:
    nombre: str
    precio: int
    id_producto: Optional[int] = None
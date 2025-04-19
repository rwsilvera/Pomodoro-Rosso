from dataclasses import dataclass
from typing import Optional

@dataclass
class Ingrediente:
    nombre: str
    unidad_medida: str
    id_ingrediente: Optional[int] = None
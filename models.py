from dataclasses import dataclass
from typing import Optional


@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    cidade: str
    id: Optional[int] = None


@dataclass
class Produto:
    nome: str
    codigo: str
    preco: float
    quantidade: int
    id: Optional[int] = None 
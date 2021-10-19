from dataclasses import dataclass
from typing import List

@dataclass
class Expr:
    def __repr__(self) -> str:
        return str(self)

@dataclass
class SymbolMeta(Expr):
    var: str

@dataclass
class AddMeta(Expr):
    operands: List[Expr]

@dataclass
class MulMeta(Expr):
    operands: List[Expr]

from dataclasses import dataclass
from typing import List

@dataclass
class Expr:
    pass

@dataclass
class SymbolMeta(Expr):
    var: str

@dataclass
class AddMeta(Expr):
    operands: List[Expr]

@dataclass
class MulMeta(Expr):
    operands: List[Expr]

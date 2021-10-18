from .base import SymbolMeta
from . import add
from . import mul

class Symbol(SymbolMeta):
    def __add__(self, other):
        if isinstance(other, add.Add):
            return other + self
        elif isinstance(other, Symbol) and self == other:
            return mul.Mul([2, Symbol(self.var)])
        else:
            return add.Add([self, other])
    def __str__(self):
        return str(self.var)
from .base import MulMeta
from . import symbol as sym
from . import add

class Mul(MulMeta):
    def precedance(self, a):
        match a:
            case int():
                return (0,)
            case float():
                return (0,)
            case sym.Symbol(var):
                return (1, var)
            case add.Add(operands):
                return (2, *map(self.precedance, operands))
            case Mul(operands):
                return (3, *map(self.precedance, operands))
            case _:
                return float('inf')
    def sort(self):
        self.operands.sort(key=self.precedance)
    def __str__(self):
        return '('+'*'.join(map(str, self.operands))+')'
    def __repr__(self) -> str:
        return '('+'*'.join(map(str, self.operands))+')'

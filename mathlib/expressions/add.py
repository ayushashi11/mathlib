from .base import AddMeta
from . import symbol as sym
from . import mul
from .number import ANYNUMBER

class Add(AddMeta):
    def __add__(self, other):
        if isinstance(other, Add):
            return Add([*self.operands, *other.operands])
        elif isinstance(other, sym.Symbol) and other in self.operands:
            res = [*self.operands]
            res.remove(other)
            res.append(mul.Mul([2, other]))
            return Add(res)
        elif isinstance(other, mul.Mul) and mul.Mul([ANYNUMBER, *other.operands[1:]]) in self.operands:
            res = [*self.operands]
            res.pop(mul.Mul([ANYNUMBER, *other.operands[1:]]))
            res.append(mul.Mul([2, other]))
            return Add(res)
        else:
            return Add([*self.operands, other])
    def __str__(self):
        return '('+'+'.join(map(str, self.operands))+')'

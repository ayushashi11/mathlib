from .base import AddMeta
from . import symbol as sym
from . import mul
from .number import ANYNUMBER

class Add(AddMeta):
    def __add__(self, other):
        if isinstance(other, Add):
            print("two adds")
            return Add([*self.operands, *other.operands])
        elif isinstance(other, sym.Symbol) and other in self.operands:
            res = [*self.operands]
            res.remove(other)
            res.append(mul.Mul([2, other]))
            return Add(res)
        elif isinstance(other, sym.Symbol) and mul.Mul([ANYNUMBER, other]) in self.operands:
            res = [*self.operands]
            i = res.index(mul.Mul([ANYNUMBER, other]))
            op = res[i].operands
            res.remove(mul.Mul([ANYNUMBER, other]))
            res.append(mul.Mul([op[0]+1, other]))
            return Add(res)
        elif isinstance(other, mul.Mul) and len(other.operands)==2:
            res = [*other.operands]
            print(res)
            if res[1] in self.operands:
                res1 = [*self.operands]
                res1.remove(res[1])
                res1.append(mul.Mul([res[0]+1, res[1]]))
                return Add(res1)
            elif mul.Mul([ANYNUMBER, res[1]]) in self.operands:
                res1 = [*self.operands]
                i = res1.index(mul.Mul([ANYNUMBER, res[1]]))
                op = res1[i].operands
                res1.remove(mul.Mul([ANYNUMBER, res[1]]))
                res1.append(mul.Mul([op[1]+res[0], res[1]]))
                return Add(res1)
            return Add([*self.operands, other])
        elif isinstance(other, mul.Mul) and mul.Mul([ANYNUMBER, *other.operands[1:]]) in self.operands:
            res = [*self.operands]
            i = res.index(mul.Mul([ANYNUMBER, *other.operands[1:]]))
            op = res[i].operands
            res.remove(mul.Mul([ANYNUMBER, *other.operands[1:]]))
            res.append(mul.Mul([op[0]+other.operands[0], *res[1:]]))
            return Add(res)
        else:
            print("else")
            return Add([*self.operands, other])
    def __str__(self):
        return '('+'+'.join(map(str, self.operands))+')'
    def __repr__(self) -> str:
        return '('+'+'.join(map(str, self.operands))+')'

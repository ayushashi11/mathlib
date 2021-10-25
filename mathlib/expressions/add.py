from .base import AddMeta
from . import symbol as sym
from . import mul
from .number import ANYNUMBER

class Add(AddMeta):
    def precedance(self, a):
        match a:
            case int():
                return (0,)
            case float():
                return (0,)
            case sym.Symbol(var):
                return (1, var)
            case Add(operands):
                return (2, *map(self.precedance, operands))
            case mul.Mul(operands):
                return (3, *map(self.precedance, operands))
            case _:
                return float('inf')
    def sort(self):
        self.operands.sort(key=self.precedance)
    def __add__(self, other):
        self.sort()
        if isinstance(other, Add):
            print("two adds")
            other.sort()
            i=0
            j=0
            ret = []
            while i<len(self.operands) and j<len(self.operands):
                match self.operands[i], other.operands[j]:
                    case (int(), int())|(int(), float())|(float(), int())|(float(), float()):
                        ret.append(self.operands[i]+other.operands[j])
                        i+=1
                        j+=1
                    case (sym.Symbol(v1), sym.Symbol(v2)) if v1==v2:
                        ret.append(mul.Mul([2,sym.Symbol(v1)]))
                        i+=1
                        j+=1
                    case _:
                        ret.append(self.operands[i])
                        i+=1
            while i<len(self.operands):
                ret.append(self.operands[i])
                i+=1
            while j<len(other.operands):
                ret.append(other.operands[j])
                j+=1
            return Add(ret)

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

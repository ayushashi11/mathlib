from .base import MulMeta

class Mul(MulMeta):
    def __str__(self):
        return '('+'*'.join(map(str, self.operands))+')'
    def __repr__(self) -> str:
        return '('+'*'.join(map(str, self.operands))+')'

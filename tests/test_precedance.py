from mathlib import Add
from mathlib.expressions.symbol import Symbol

def test_precedance():
    assert Add([]).precedance(145789)==(0,)
    assert Add([]).precedance(Symbol('x')+1)==(2,(0,),(1,'x'))
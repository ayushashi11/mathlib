from mathlib import Symbol

def test_symbol():
    assert Symbol('x').var == 'x'
    assert Symbol('x') == Symbol('x')

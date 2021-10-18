from .expressions import Symbol, ANYNUMBER

x = Symbol('x')
exp0 = x+1
print(x+exp0)

lis = [7,8,6,8,9,5,8]
lis.pop(ANYNUMBER)
print(lis)

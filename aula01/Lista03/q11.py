B = 7
A = 2
C = 3.5
L = bool(False)
V = bool(True)

a = B == A * C and (L and V)
b = B > A or B == A**A
c = L and B / A >= C
d = not L or V and (A+B)**0.5 >= C
e = B / A == C or B / A != C
f = L or B**A <= C * 10 + A * B

print('A letra a é:', a)
print('A letra b é:', b)
print('A letra c é:', c)
print('A letra d é:', d)
print('A letra e é:', e)
print('A letra f é:', f)


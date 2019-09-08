"""
Original file iteration failed to function as the math sqrt function cannot handle negative values. Imported cmath
to handle the problem.
"""

from cmath import sqrt

a = 2
b = 1
c = 2

q = b**2 - 4*a*c
q_sr = sqrt(q)

x1 = (-b + q_sr)/2*a
x2 = (-b - q_sr)/2*a
print(x1, x2)
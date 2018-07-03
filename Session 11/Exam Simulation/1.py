import math

def mysin(n):
    'Maclaurin Series'
    return (-1)**n * x**(2*n + 1)/math.factorial(2*n + 1)

n = 10
s = 0
x = math.pi/3

for i in range(n + 1):
    s += mysin(i)

exact = math.sin(x)
error = (exact-s)
print(exact)
print(s)
print(error)

import cmath
import math
z=complex(input())
print(abs(z))
arg=math.atan(z.real/z.imag)
print(arg)
print(z.conjugate())


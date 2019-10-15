import cmath
z=1j
print(cmath.sin(z).real,"\t",cmath.sin(z).imag)
print(cmath.cos(z).real,"\t",cmath.cos(z).imag)

print(cmath.sin(z)**2)
print(cmath.cos(z)**2)
a=cmath.sin(z)**2+cmath.cos(z)**2
print("Zależność nie jest spełniona ponieważ wynik wynosi: ", a)

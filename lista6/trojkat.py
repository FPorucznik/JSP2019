import math
def obwod(a,b,c):
    return a+b+c

def pole(a,b,c):
    polObwodu=(a+b+c)/2
    p=math.sqrt(polObwodu*(polObwodu-a)*(polObwodu-b)*(polObwodu-c))
    return p

def jakiBoczny(a,b,c):
    if a==b==c:
        return 'Trójkąt równoboczny'
    elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a):
        return 'Trójkąt równoramienny'
    else:
        return 'Trójąt różnoboczny'

jakiBoczny(1,1,2)
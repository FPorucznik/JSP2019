import math
def obwod(a,b,c):
    return 'obwód: '+a+b+c

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

def jakiKatny(a,b,c):
    boki=[]
    boki.append(a)
    boki.append(b)
    boki.append(c)
    najdluzszy=max(boki)
    boki.remove(najdluzszy)
    if najdluzszy**2>boki[0]**2+boki[1]**2:
        return 'Trójkąt rozwartokątny'
    elif najdluzszy**2==boki[0]**2+boki[1]**2:
        return 'Trójkąt prostokątny'
    else:
        return 'Trójkąt ostrokątny'
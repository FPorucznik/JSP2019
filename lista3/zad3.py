import math
a=int(input())
b=int(input())
c=int(input())
def kwadratowa(a,b,c):

    if a==0:
        print("To nie jest równanie kwadratowe!")
    else:
        delta=b**2-(4*a*c)
        if(delta>0):
            x1=(-b-math.sqrt(delta))/(2*a)
            x2=(-b+math.sqrt(delta))/(2*a)
            wynik=(x1,x2)
            print(wynik)
        elif(delta==0):
            x2="brak"
            x1=(-b)/(2*a)
            wynik=(x1,x2)
            print(wynik)
        else:
            print("brak pierwiastkow")

kwadratowa(a,b,c)
        


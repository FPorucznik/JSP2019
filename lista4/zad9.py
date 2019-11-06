n=int(input())
while n<=0:
    n=int(input("Podaj dodatnia liczbe calkowita: "))
wynik=1
for i in range(1,n+1):
    wynik*=i
print(wynik)
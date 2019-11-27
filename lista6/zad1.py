import trojkat
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print('Obwód: ',trojkat.obwod(a,b,c))
    print('Pole: ',trojkat.pole(a,b,c))
    print(trojkat.jakiBoczny(a,b,c))
    print(trojkat.jakiKatny(a,b,c))
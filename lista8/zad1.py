from datetime import date
import os
def szyfrCezara(zdanie, przesuniecie):
    litery=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    kody=[]
    ciag=[]
    zdanie=zdanie.lower()
    for i in litery:
        kody.append(ord(i))
    slownik=dict(zip(kody,litery))
    for i in zdanie:
        ciag.append(ord(i))
    for i in ciag:
        if i in slownik:
            pre=96
            nr=ciag.index(i)
            if i+przesuniecie>122:
                start=(i+przesuniecie)-122
                start+=pre
                ciag[nr]=chr(start)
            else:
                ciag[nr]=chr(i+przesuniecie)
        else:
            nr=ciag.index(i)
            ciag[nr]=chr(i)
    return ''.join(ciag)

sciezka=input('Ścieżka:')
n=int(input('Przesunięcie(1-10):'))
while n<1 or n>10:
    n=int(input('Przesunięcie(1-10):'))
try:
    plik=open(sciezka,'r')
    tekst=plik.read()
except IOError:
    print("Błąd odczytu")
else:
    today=date.today()
    zaszyfrowanyTekst=szyfrCezara(tekst,n)
    katalog=input('Ścieżka katalogu:')
    if os.path.isdir(katalog):
        katalog+='\plik_zaszyfrowany'+str(n)+'_'+str(today.year)+str(today.month)+str(today.day)+'.txt'
        try:
            nowy=open(katalog,'w')
            nowy.write(zaszyfrowanyTekst)
            nowy.close()
        except IOError:
            print("Błąd zapisu")
    else:
        try:
            os.mkdir(katalog)
            katalog+='\plik_zaszyfrowany'+str(n)+'_'+str(today.year)+str(today.month)+str(today.day)+'.txt'
            nowy=open(katalog,'w')
            nowy.write(zaszyfrowanyTekst)
            nowy.close()
        except OSError:
            print("Błąd otwarcia/tworzenia katalogu")
        except IOError:
            print("Błąd zapisu")
        

    








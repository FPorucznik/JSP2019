from datetime import date
import os
def deszyfrCezara(zdanie, przesuniecie):
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
            pre=123
            nr=ciag.index(i)
            if i-przesuniecie<97:
                start=(i-przesuniecie)-97
                start+=pre
                ciag[nr]=chr(start)
            else:
                ciag[nr]=chr(i-przesuniecie)
        else:
            nr=ciag.index(i)
            ciag[nr]=chr(i)
    return ''.join(ciag)

sciezka=input('Ścieżka:')
try:
    pliki=os.listdir(sciezka)
except OSError:
    print("Błąd odczytu katalogu")
else:
    for i in pliki:
        if 'plik_zaszyfrowany' in i:
            if i[17:18]=='1' and i[18:19]=='0':
                n=10
                sciezka2=sciezka+'\\'+i
                try:
                    plik=open(sciezka2,'r')
                    tekst=plik.read()
                except IOError:
                    print("Błąd odczytu")
                else:
                    today=date.today()
                    deszyfrowanyTekst=deszyfrCezara(tekst,n)
                    sciezkaFinal=sciezka+'\plik_deszyfrowany'+str(n)+'_'+str(today.year)+str(today.month)+str(today.day)+'.txt'
                    try:
                        nowy=open(sciezkaFinal,'w')
                        nowy.write(deszyfrowanyTekst)
                        nowy.close()
                    except OSError:
                        print("Błąd otwarcia katalogu")
                    except IOError:
                        print("Błąd zapisu")
            else:
                n=int(i[17:18])
                sciezka2=sciezka+'\\'+i
                try:
                    plik=open(sciezka2,'r')
                    tekst=plik.read()
                except IOError:
                    print("Błąd odczytu")
                else:
                    today=date.today()
                    deszyfrowanyTekst=deszyfrCezara(tekst,n)
                    sciezkaFinal=sciezka+'\plik_deszyfrowany'+str(n)+'_'+str(today.year)+str(today.month)+str(today.day)+'.txt'
                    try:
                        nowy=open(sciezkaFinal,'w')
                        nowy.write(deszyfrowanyTekst)
                        nowy.close()
                    except OSError:
                        print("Błąd otwarcia katalogu")
                    except IOError:
                        print("Błąd zapisu")


    








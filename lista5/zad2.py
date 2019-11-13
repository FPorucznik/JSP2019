klucz={1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'pięć',6:'sześć',7:'siedem',8:'osiem',9:'dziewięć',10:'dziesięć',11:'jedenaście',12:'dwanaście',13:'trzynaście',14:'czternaście',15:'piętnaście',16:'szesnaście',17:'siedemnaście',18:'osiemnaście',19:'dziewiętnaście',20:'dwadzieścia',30:'trzydzieści',40:'czterdzieści',50:'pięćdziesiąt',60:'sześćdziesiąt',70:'siedemdziesiąt',80:'osiemdziesiąt',90:'dziewięćdziesiąt',100:'sto',200:'dwieście',300:'trzysta',400:'czterysta',500:'pięćset',600:'sześćset',700:'siedemset',800:'osiemset',900:'dziewięćset',1000:'tysiąc'}

def zamiana(liczba):
    wynik=''
    if liczba in klucz:
        wynik=klucz.get(liczba)
    elif len(str(liczba))==2:
        cz1=str(liczba)
        nowa1=int(cz1[0])*10
        nowa2=int(cz1[1])
        if nowa1 in klucz:
            wynik=klucz.get(nowa1)
            wynik+=' '+klucz.get(nowa2)
    elif len(str(liczba))==3:
        cz1=str(liczba)
        nowa1=int(cz1[0])*100
        nowa2=int(cz1[1])*10
        nowa3=int(cz1[2])
        if nowa1 in klucz:
            wynik=klucz.get(nowa1)
            if nowa2==10 and nowa2 in klucz:
                koniec=nowa2+nowa3
                wynik+=' '+klucz.get(koniec)
                nowa3=0
            elif nowa2 in klucz:
                wynik+=' '+klucz.get(nowa2)
            if nowa3 in klucz:
                wynik+=' '+klucz.get(nowa3)
    elif len(str(liczba))==4:
        cz1=str(liczba)
        nowa1=int(cz1[0])*1000
        nowa2=int(cz1[1])*100
        nowa3=int(cz1[2])*10
        nowa4=int(cz1[3])
        if nowa1 in klucz:
            wynik=klucz.get(nowa1)
            if nowa2 in klucz:
                wynik+=' '+klucz.get(nowa2)
            if nowa3==10 and nowa3 in klucz:
                koniec=nowa3+nowa4
                wynik+=' '+klucz.get(koniec)
                nowa4=0
            elif nowa3 in klucz:
                wynik+=' '+klucz.get(nowa3)
            if nowa4 in klucz:
                wynik+=' '+klucz.get(nowa4)
    print(wynik)
    return wynik

assert zamiana(1511)=='tysiąc pięćset jedenaście','Nie działa'
assert zamiana(698)=='sześćset dziewięćdziesiąt osiem','Nie działa'

zamiana(101)
from xml.dom import minidom

class KantorDane():
    def __init__(self,path):
        self.myDoc=minidom.parse(path)
    def dane(self):
        nazwaTag=self.myDoc.getElementsByTagName('nazwa_waluty')
        przelicznikTag=self.myDoc.getElementsByTagName('przelicznik')
        kodWalutyTag=self.myDoc.getElementsByTagName('kod_waluty')
        kursSredniTag=self.myDoc.getElementsByTagName('kurs_sredni')
        nazwy=[]
        przeliczniki=[]
        kody=[]
        kursy=[]
        for elem in nazwaTag:
            nazwy.append(elem.firstChild.data)
        for elem in przelicznikTag:
            przeliczniki.append(elem.firstChild.data)
        for elem in kodWalutyTag:
            kody.append(elem.firstChild.data)
        for elem in kursSredniTag:
            kursy.append(elem.firstChild.data)
        kodWaluty=[]
        for i in range(len(przeliczniki)):
            current=[' '.join([przeliczniki[i],kody[i]])]
            kodWaluty.append(current)
        for i in range(0, len(kursy)): 
            current=kursy[i].maketrans
            new=kursy[i].translate(current(',','.'))
            kursy[i]=new
            kursy[i]=float(kursy[i])
        return nazwy, przeliczniki, kodWaluty, kursy

class KantorKonwersja():
    def __init__(self,pln,inna,wybrana1,wybrana2):
        self.pln=pln
        self.inna=inna
        self.wybrana1=wybrana1
        self.wybrana2=wybrana2
    def plnNaWybrana(self):
        pln=float(self.pln)
        wybranaWaluta=self.wybrana1
        dane=KantorDane('D:\Listy Python\JSP2019\lista10\kursy.xml')
        nazwy,przeliczniki,kodWaluty,kursy=dane.dane()
        waluta_Kurs= dict(zip(nazwy,kursy))
        wynik=0.0
        przelicznik=0.0
        for i in range(0,len(nazwy)):
            if nazwy[i]==wybranaWaluta:
                przelicznik=float(przeliczniki[i])
        for key in waluta_Kurs:
            if key==wybranaWaluta:
                kurs=waluta_Kurs.get(key)
                wynik=(pln/kurs)*przelicznik
        return wynik
    def wybranaNaWybrana(self):
        ilosc=float(self.inna)
        wybrana1=self.wybrana1
        wybrana2=self.wybrana2
        dane=KantorDane('D:\Listy Python\JSP2019\lista10\kursy.xml')
        nazwy,przeliczniki,kodWaluty,kursy=dane.dane()
        waluta_Kurs= dict(zip(nazwy,kursy))
        wynik=0.0
        przelicznik1=0.0
        przelicznik2=0.0
        naPln=0.0
        for i in range(0,len(nazwy)):
            if nazwy[i]==wybrana1:
                przelicznik1=float(przeliczniki[i])
            elif nazwy[i]==wybrana2:
                przelicznik2=float(przeliczniki[i])
        for key in waluta_Kurs:
            if key==wybrana1:
                kurs=waluta_Kurs.get(key)
                naPln=(ilosc*kurs)/przelicznik1
        for key in waluta_Kurs:
            if key==wybrana2:
                kurs=waluta_Kurs.get(key)
                wynik=(naPln/kurs)*przelicznik2
        return wynik
        
opcja=int(input('Wybierz opcję:\n1-lista dostępnych kursów\n2-konwersja PLN <-> wybrana waluta\n3-konwersja wybrana waluta <-> wybrana waluta\n'))
if opcja==1:
    lista=KantorDane('D:\Listy Python\JSP2019\lista10\kursy.xml')
    nazwy,przeliczniki,kodWaluty,kursy=lista.dane()
    kodWaluty=[y for x in kodWaluty for y in x]
    dane=[nazwy,kodWaluty,kursy]
    for i in range(0,len(nazwy)):
        print('%35s'% nazwy[i],'\t','%9s'% kodWaluty[i],'\t','%6s'% kursy[i])
elif opcja==2:
    pln=float(input('Podaj liczbę PLN: '))
    wybranaWaluta=input('Wpisz nazwę waluty: ')
    konwersja=KantorKonwersja(pln,'',wybranaWaluta,'')
    print(pln,' PLN = ','%.2f'%konwersja.plnNaWybrana(),' ',wybranaWaluta)
elif opcja==3:
    ilosc=float(input('Podaj liczbę swojej waluty: '))
    wybranaWaluta1=input('Wpisz nazwę waluty: ')
    wybranaWaluta2=input('Na jaką walutę konwersja?: ')
    konwersja=KantorKonwersja('',ilosc,wybranaWaluta1,wybranaWaluta2)
    print(ilosc,' ',wybranaWaluta1,' = ','%.2f'%konwersja.wybranaNaWybrana(),' ',wybranaWaluta2)

    
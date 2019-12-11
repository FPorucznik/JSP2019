import os
cwd=os.getcwd()
try:
    plik=open(cwd+'\PESEL.txt','r')
except IOError:
    print('Brak pliku')
else:
    pesele=[]
    for i in plik:
        pesele.append(i)
    pesele=list(map(lambda s: s.strip(), pesele))
    for i in pesele:
        sprawdzany=i
        kontrolna=int(i[10:])
        testowa=0
        wyniki=[]
        doSpr=list(sprawdzany[0:10])
        waga=[1,3,7,9]
        licznik=0
        for j in doSpr:
            if licznik==0 or licznik==4 or licznik==8:
                wyniki.append(int(j)*waga[0])
            elif licznik==1 or licznik==5 or licznik==9:
                wyniki.append(int(j)*waga[1])
            elif licznik==2 or licznik==6:
                wyniki.append(int(j)*waga[2])
            elif licznik==3 or licznik==7:
                wyniki.append(int(j)*waga[3])
            licznik+=1
        for g in wyniki:
            if len(str(g))==2:
                ind=wyniki.index(g)
                nowa=str(g)
                nowa=int(nowa[1:])
                wyniki[ind]=nowa
        suma=sum(wyniki)
        suma=str(suma)
        if len(suma)==2:
            druga=int(suma[1:])
            testowa=10-druga
        else:
            testowa=10-int(suma)
        if testowa==kontrolna:
            nrPlci=str(i)
            nrPlci=int(nrPlci[9:10])
            dzien=i[4:6]
            mies=i[2:4]
            rok=i[:2]
            if nrPlci==0 or nrPlci%2==0:
                plec='kobieta'
                if mies[0]=='2':
                    m2='0'+mies[1]
                    r2='20'+rok
                elif mies[0]=='3':
                    m2='1'+mies[1]
                    r2='20'+rok
                else:
                    m2=mies
                    r2='19'+rok
                dobrePesele=open(cwd+'\dobrePESELE.txt','a')
                dobrePesele.write("nr PESEL:\n data urodzenia "+dzien+'-'+m2+'-'+r2+';\t płeć: '+plec+'\n')
                dobrePesele.close()   
            else:
                plec='mężczyzna'
                if mies[0]=='2':
                    m2='0'+mies[1]
                    r2='20'+rok
                elif mies[0]=='3':
                    m2='1'+mies[1]
                    r2='20'+rok
                else:
                    m2=mies
                    r2='19'+rok
                dobrePesele=open(cwd+'\dobrePESELE.txt','a')
                dobrePesele.write("nr PESEL:\n data urodzenia "+dzien+'-'+m2+'-'+r2+';\t płeć: '+plec+'\n')
                dobrePesele.close()  
            



        
        
    

        
    
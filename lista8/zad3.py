import random
import os
cwd=os.getcwd()
print(cwd)
plik=open(cwd+'\PESEL.txt','w')
plik.close()

for i in range(10):
    pesel=''
    rok=str(random.randint(1900,2099))
    pesel+=str(rok[1:3])
    miesiac=str(random.randint(1,12))
    if int(rok)>=2000:
        if len(miesiac)==1 and int(miesiac)<10:
            pesel+='2'+miesiac
        elif int(miesiac)>=10:
            pesel+='3'+miesiac[1:2]
    else:
        if len(miesiac)==1:
            pesel+='0'+miesiac
        else:
            pesel+=miesiac
    dzien=str(random.randint(1,31))
    if len(dzien)==1:
        pesel+='0'+dzien
    else:
        pesel+=dzien
    porzadkowa=str(random.randint(0,9999))
    if len(porzadkowa)==1:
        pesel+='000'+porzadkowa
    elif len(porzadkowa)==2:
        pesel+='00'+porzadkowa
    elif len(porzadkowa)==3:
        pesel+='0'+porzadkowa
    else:
        pesel+=porzadkowa
    kontrolna=str(random.randint(0,9))
    pesel+=kontrolna
    peselTxt=open(cwd+'\PESEL.txt','a')
    peselTxt.write(pesel+'\n')
    peselTxt.close()

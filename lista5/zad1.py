import re
klucz={'jeden':1,'dwa':2,'trzy':3,'cztery':4,'pięć':5,'sześć':6,'siedem':7,'osiem':8,'dziewięć':9,'dziesięć':10,'jedenaście':11,'dwanaście':12,'trzynaście':13,'czternaście':14,'piętnaście':15,'szesnaście':16,'siedemnaście':17,'osiemnaście':18,'dziewiętnaście':19,'dwadzieścia':20,'trzydzieści':30,'czterdziesci':40,'pięćdziesiąt':50}
def zamiana(slowo):
    wynik=0
    if slowo in klucz and len(slowo)<=8:
        wynik=klucz.get(slowo)
    elif '_' in slowo:
        nowe=re.split('_',slowo)
        cz1=nowe[0]
        cz2=nowe[1]
        if cz1 in klucz:
            wynik+=klucz.get(cz1)
        if cz2 in klucz:
            wynik+=klucz.get(cz2)
    elif len(slowo)>8:
        if slowo in klucz:
            wynik=klucz.get(slowo)      
    print(wynik)
    return wynik


assert zamiana('jeden')==1,'Nie działa'
assert zamiana('trzydzieści_trzy')==33,'Nie działa'  
assert zamiana('trzynaście')==13,'Nie działa'

zamiana('dziewiętnaście')

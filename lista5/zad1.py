klucz={'jeden':1,'dwa':2,'trzy':3,'cztery':4,'pięć':5,'sześć':6,'siedem':7,'osiem':8,'dziewięć':9,'dziesięć':10,'jedenaście':11,'dwanaście':12,'trzynaście':13,'czternaście':14,'piętnaście':15,'szesnaście':16,'siedemnaście':17,'osiemnaście':18,'dziewiętnaście':19,'dwadzieścia':20,'trzydziesci':30,'czterdziesci':40,'pięćdziesiąt':50}
def zamiana(slowo):
    wynik=0
    for key in klucz.keys():
        if slowo==key and len(key)<=8:
            wynik=klucz.get(key)
        elif '_' in slowo:
            
    print(wynik)
def test(tekst):
    print(len(tekst))
zamiana('trzydzieści_trzy')

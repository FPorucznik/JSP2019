def nastElem(x):
    wynik=[]
    i=0
    while i<len(x):
        licznik=1
        while i+1<len(x) and x[i]==x[i+1]:
            i+=1
            licznik+=1
        wynik.append(str(licznik)+x[i])
        i+=1
    return ''.join(wynik)

el='1'
n=int(input())
for i in range(n):
    el=nastElem(el)
    print(el)
klucz={'a':'y','e':'i','i':'o','o':'a','y':'e',}
klucz_deszyfr={v: k for k, v in klucz.items()}


def szyfr(tekst):
    tekst=list(tekst)
    nowy=[]
    for i in tekst:
        if i in klucz:
            x=klucz.get(i)
            nowy.append(x)
        else:
            nowy.append(i)
            
    print(nowy)

def deszyfr(tekst):
    tekst=list(tekst)
    nowy=[]
    for i in tekst:
        if i in klucz_deszyfr:
            x=klucz_deszyfr.get(i)
            nowy.append(x)
        else:
            nowy.append(i)
            
    print(nowy)

szyfr('to jest moj tekst')
deszyfr('ta jist maj tikst')
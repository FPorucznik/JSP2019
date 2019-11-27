def szyfrCezara(zdanie):
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
            nr=ciag.index(i)
            if i==122:
                ciag[nr]=chr(98)
            elif i==121:
                ciag[nr]=chr(97)
            else:
                ciag[nr]=chr(i+2)
        else:
            nr=ciag.index(i)
            ciag[nr]=chr(i)
    return ''.join(ciag)

def deszyfrCezara(zdanie):
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
            nr=ciag.index(i)
            if i==97:
                ciag[nr]=chr(121)
            elif i==98:
                ciag[nr]=chr(122)
            else:
                ciag[nr]=chr(i-2)
        else:
            nr=ciag.index(i)
            ciag[nr]=chr(i)
    return ''.join(ciag)

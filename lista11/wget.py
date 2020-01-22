import urllib.request
from urllib.parse import urlparse
l=input("Podaj URL: ")
def zapis(link):
    o=urlparse(link)
    path=o.path
    name=[]
    if path.endswith("/"):
        name='index.html'
    else:
        length=len(path)-1
        while path[length] != '/':
            name.append(path[length]) 
            length-=1
        name=''.join(list(reversed(name)))+'.html'
    urllib.request.urlretrieve(link, name)
print(zapis(l))
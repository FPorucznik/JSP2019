import urllib.request
from urllib.parse import urlparse
l=input("Podaj URL: ")
def zapis(link):
    try:
        with urllib.request.urlopen(link) as url:
            parsed=urlparse(link)
            s=url.read()
            return parse
            #sOut = open()
    except urllib.error.HTTPError:
        return "Strona nie została znaleziona"
    except urllib.error.URLError:
        return "Strona nie została znaleziona"

zapis(url)

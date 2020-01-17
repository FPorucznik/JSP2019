import urllib.request
try:
    with urllib.request.urlopen('http://www.wp.pl') as url:
        print("Odczytano stronę")
except urllib.error.HTTPError:
    print("Strona nie została znaleziona")
except urllib.error.URLError:
    print("Strona nie została znaleziona")

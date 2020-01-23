import re
text = 'Przykładowy tekst z adresami: http://www.wp.pl i kolejny adres https://facebook.com'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Adresy: ",urls)
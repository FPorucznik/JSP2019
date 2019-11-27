import SzyfrCezara
zdanie=input()
zaszyfrowane=SzyfrCezara.szyfrCezara(zdanie)
deszyfrowane=SzyfrCezara.deszyfrCezara(zaszyfrowane)
print('Zaszyfrowane: ',zaszyfrowane)
print('Deszyfrowane: ',deszyfrowane)
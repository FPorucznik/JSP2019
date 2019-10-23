lista=['Kasia','Basia','Marek','Darek']
print(lista)
lista.append('Józek')
print(lista)
a=['Ania','Basia']
lista.extend(a)
print(lista)
lista=sorted(lista)
print(lista)
print(lista[3],'\n',lista[:2],'\n',lista[-2:])
for x in range(lista.count('Basia')):
    lista.remove('Basia')
print(lista)
liczbaStudentow=len(lista)
print(liczbaStudentow)
lista=tuple(lista)
print(lista)
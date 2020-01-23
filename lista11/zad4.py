import re
text = "Ala ma kota aczkolwiek Eryk go nie ma ehh trudno"
slowaA=re.findall(r'\b[aA]\w+', text)
slowaE=re.findall(r'\b[eE]\w+', text)
slowa=slowaA+slowaE
print(slowa)
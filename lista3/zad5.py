import re
haslo=input("Podaj hasło: ")
a=re.search("[a-z]",haslo)
b=re.search("[A-Z]",haslo)
c=re.search("[0-9]",haslo)
d=re.search("[$#@]",haslo)
if(not a or not b or not c or not d or len(haslo)<6 or len(haslo)>16):
    print("zle hasło")
else:
    print("dobre hasło")
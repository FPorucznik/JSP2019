import math
def konwerter(wartosc,naCo):
    if naCo=="deg":
        wynik=math.degrees(wartosc)
        print(wartosc," radianow = ",wynik," stopni")
    elif naCo=="rad":
        wynik=math.radians(wartosc)
        print(wartosc," stopni = ",wynik," radianow")

#konwersja stopni na radiany-"rad", a na odwrót-"deg"
konwerter(45,"rad")

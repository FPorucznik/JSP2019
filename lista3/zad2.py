def spr_z_if():
    liczba=int(input())
    if liczba%2==0:
        print("parzysta")
    else:
        print("nieparzysta")

def spr_bez_if():
    liczba=int(input())
    parzystosc=['parzysta','nieparzysta']
    reszta=liczba%2
    print(parzystosc[reszta])


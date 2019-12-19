import numpy as np
import matplotlib.pyplot as plt

v0 = int(input("Wprowadz predkosc poczatkowa [m/s]: "))
alfa = int(input("Wprowadz kat [stopnie]: "))

print(np.cos(alfa*np.pi/180))

v0x = v0 * np.cos(alfa * np.pi / 180)
v0y = v0 * np.sin(alfa * np.pi / 180)
g = 9.81
Vy = list()
T = list()
Vx = list()
S = list()
Sy = list()

Hmax = v0y**2/(2*g)
Z = (2*(v0**2)*np.sin(alfa * np.pi / 180)*np.cos(alfa * np.pi / 180))/g
Ts = (2*v0y) / g
print("Wysokosc maks: " + str(Hmax) + " metrow")
print("Zasieg: " + str(Z) + " metrow")
print("Czas spadania: " + str(Ts) + " sekund")


def getVy(v0x, v0y, Ts):
    for i in np.arange(0, Ts, 0.01):
        Vy.append(v0y - (g*i))
        T.append(i)
        Vx.append(v0x)

def getS(v0x, Ts):
    for i in np.arange(0, Ts, 0.01):
        S.append(v0x*i)

def getSy(v0y, Ts):
    for i in np.arange(0, Ts, 0.01):
        Sy.append(v0y * i - (g*(i**2)) / 2)


fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)

getVy(v0x, v0y, Ts)
getS(v0x, Ts)
getSy(v0y, Ts)
ax1.plot(T, Vy)
ax2.plot(T, Vx)
ax3.plot(S, T)
ax4.plot(S, Sy)
plt.show()
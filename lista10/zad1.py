import numpy as np
class Kolo():
    def __init__(self,r):
        self.promien=r
    def pole(self):
        pole=np.pi*self.promien**2
        return pole
    def obwod(self):
        obwod=2*np.pi*self.promien
        return obwod

testoweKolo=Kolo(5)
print('Pole: ',testoweKolo.pole())
print('Obwód: ',testoweKolo.obwod())
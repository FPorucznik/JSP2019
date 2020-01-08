from itertools import combinations
class Lista():
    def __init__(self,l):
        self.lista=l
    def podlisty(self):
        podlisty=[]
        for i in range(len(self.lista)+1):
            podlista=[list(x) for x in combinations(self.lista,i)]
            podlisty.extend(podlista)
        return podlisty

testowaLista=Lista([1,2,3])
print(testowaLista.podlisty())
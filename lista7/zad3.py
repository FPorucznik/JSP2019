import time
import random
posortowane1=[]
posortowane2=[]
posortowane3=[]
for i in range(100):
    los=random.randint(0,20)
    posortowane1.append(los)
for i in range(200):
    los=random.randint(0,20)
    posortowane2.append(los)
for i in range(300):
    los=random.randint(0,20)
    posortowane3.append(los)
def sort_bab(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

start=time.time()
sort_bab(posortowane1)
print(posortowane1)
end=time.time()-start
print(end,'\n--------------')
start=time.time()
sort_bab(posortowane2)
print(posortowane2)
end=time.time()-start
print(end,'\n--------------')
start=time.time()
sort_bab(posortowane3)
print(posortowane3)
end=time.time()-start
print(end)
        
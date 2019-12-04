import time
import random
def sort_wst(x):
    posortowane=[]
    for i in range(x):
        los=random.randint(0,20)
        posortowane.append(los)
    #print(posortowane)

    for i in range(1,len(posortowane)):
        aktualny=posortowane[i]
        pozycja=i

        while pozycja>0 and posortowane[pozycja-1]>aktualny:
            posortowane[pozycja]=posortowane[pozycja-1]
            pozycja-=1
        posortowane[pozycja]=aktualny
    return posortowane

start=time.time()
print(sort_wst(100))
end=time.time()-start
print(end,'\n--------------')
start=time.time()
print(sort_wst(200))
end=time.time()-start
print(end,'\n--------------')
start=time.time()
print(sort_wst(300))
end=time.time()-start
print(end)
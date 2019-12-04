import time
n=int(input())

def rekurencja(n):
    if n<=1:
        return n
    else:
        return rekurencja(n-1)+rekurencja(n-2)

def iteracja(n):
    if n<=1:
        return n
    else:
        fib=[0,1]
        for i in range(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
        for i in range(n+1):
            print(fib[i])
        

print('Rekurencyjnie:')
start=time.time()
for i in range(n+1):
    print(rekurencja(i))
end=time.time()-start
print('Czas: ',end,'\n--------------\nIteracyjnie:')
start=time.time()   
iteracja(n)
end=time.time()-start
print('Czas: ',end,'\n--------------') 
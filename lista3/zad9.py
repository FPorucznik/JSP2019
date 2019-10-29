m=int(input())
n=int(input())
tab = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        tab[i][j]= i*j

print(tab)
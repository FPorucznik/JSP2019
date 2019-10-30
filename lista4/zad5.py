from itertools import permutations
def perm(lista):
    for i in permutations(lista):
        print(i)
perm([1,2,3])
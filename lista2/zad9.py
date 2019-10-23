from itertools import chain
lista=[[2,5],[1,2],[4,4]]
lista=list(chain.from_iterable(lista))
print(lista)
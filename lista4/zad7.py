def ntyWiersz(n):
   wiersz = [1]
   y = [0]
   for x in range(max(n,0)):
      print(wiersz)
      wiersz=[l+r for l,r in zip(wiersz+y, y+wiersz)]
   return n>=1
ntyWiersz(4) 
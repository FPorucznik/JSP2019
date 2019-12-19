import sys
import numpy as np
def zArg():
    argumenty=sys.argv[1:]
    argumenty=[int(x) for x in argumenty]

def zPliku(arg):
    b = list()
    with open(arg) as filename:
        for line in filename:
            line = line.replace("\r\n", "")
            b.append(int(line))
    return b

def statystyki(arg):
    print(np.average(arg))
    print(np.var(arg))
    print(np.std(arg))

if ".txt" in sys.argv[1]:
    a=zPliku(sys.argv[1])
    for i in a:
        statystyki(i)
else:
    zArg()
    for i in argumenty:
        statystyki(i)
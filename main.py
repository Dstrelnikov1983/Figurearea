import Figurparsing
import os
print(os.getcwd())
#mymodule.hello()

with open('Figurlist.txt', 'r') as f:
    fig = f.read().splitlines()

l=[]

for x in fig: l.append(Figurparsing.ftodict(x))

for y in l: 
    sq=Figurparsing.squarecalc(y.get('cord'))
    y.update(square= sq)

l.sort(key=Figurparsing.getsquare)   

print (l)

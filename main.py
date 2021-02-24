import Figurparsing
import os
print(os.getcwd())
#mymodule.hello()

with open('Figurlist.txt', 'r') as f:
    fig = f.read().splitlines()

l=[]

for x in fig: l.append(Figurparsing.ftodict(x))





print (l)

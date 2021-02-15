import mymodule
import os
print(os.getcwd())
#mymodule.hello()

with open('Figurlist.txt', 'r') as f:
    fig = f.read().splitlines()

l=[]

for x in fig: l.append(mymodule.fib(x))

k=[{'type':'T','cord': [{'x':10, 'y':20},{'x':60, 'y':50}]}, 'p']

print (l)
print (k)
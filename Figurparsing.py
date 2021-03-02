# class Triangle(object):
     
#     def __init__ (self, x1,x2,y1,y2,z1,z2):
#         self.x1=x1
#         self.x2=x2
#         self.y1=y1
#         self.y2=y2
#         self.z1=z1
#         self.z2=z2

#      def printview(self):
#          return "x"

#     def square(self):  
#         return "y"


def hello():
    print('Hello, world!')

def ftodict(n):
    b={'type': n[0:1], 'cord': [cordtodict(x[1:]) for x in n[2:].split(' ')]}
    
    return b

def cordtodict(v):
    z= {'x': float(v[0:len(v)-1].split(',')[0]), 'y': float(v[0:len(v)-1].split(',')[1])}
    
    return z

def squarecalc(figurcord):
    sq=0.5*(figurcord[0].get('x')-figurcord[2].get('x'))*(figurcord[1].get('y') -figurcord[2].get('y'))
    return sq

def getsquare (cordlist):
    sq= cordlist.get('square')
    return sq

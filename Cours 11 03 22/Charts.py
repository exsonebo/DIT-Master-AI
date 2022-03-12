import math
import cmath
import matplotlib.pyplot as plt
class Poly :
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.delta = b**2 - 4*a*c
    def discriminant(self):
        return self.delta


    def racines(self):
        if(self.delta<0):
            x1 = (-self.b - cmath.sqrt(self.b)) / 2*self.a
            x2 = (-self.b + cmath.sqrt(self.b)) / 2*self.a
            print(f"x1 : {x1} et x2: {x2}")
        elif (self.delta==0):
            x0 = -self.b / 2*self.a
            print("racine double x0:",x0)
        else:
            x1 = (-self.b - math.sqrt(self.b)) / 2*self.a
            x2 = (-self.b + math.sqrt(self.b)) / 2*self.a
            print(f"x1 : {x1} et x2: {x2}")
        

    def value(self,x):
        return self.a*x**2 + self.b*x + self.c
    

f = Poly(2,4,-2)
cordonnees = {}
for i in range(-10,10):
    cordonnees[i] = f.value(i)
    
#commprehension list 
x = [x for x in cordonnees.keys()]
y = [y for y in cordonnees.values()]

print(cordonnees)
plt.axis([-100,100, -100,100])
plt.plot(x,y)
plt.show()
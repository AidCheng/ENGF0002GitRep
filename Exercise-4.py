#This program calculates the value of PI
from random import *
hits = 0
for i in range (0,100000):
    x = random()
    y = random ()
    
    if ((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5)<0.25):
        hits += 1

PI = 4 * hits / 100000
print(PI)
# Runze Cheng  / 08/Oct/2023
# This program calculates the value of PI

from random import *

def estimate_pi(precision):
    hits = 0
    total = pow(10,precision)
    
    for i in range (0,total):
        x = random()
        y = random ()
        if ((x-0.5)*(x-0.5)+(y-0.5)*(y-0.5) <= 0.25):
            hits += 1
    PI = 4 * hits / total
    return PI

precision = int(input("The number of decimal place wanted is: "))
print(estimate_pi(precision))
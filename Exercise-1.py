def gcd(a,b):
    while not a == b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

ax = int(42)
bx = int(30)
print("GCD of", ax, "and", bx, "is", gcd(ax,bx))
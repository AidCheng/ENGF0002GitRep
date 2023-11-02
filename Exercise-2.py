# Runze Cheng / 05/Oct/2023
# This program distinguishes Odd and Even numbers

def Odd_or_Even(x):
    if x%2 == 0:
        print(x,"is even")
    else:
        print(x,"is odd")

num = int(input("Input a integer: "))
Odd_or_Even(num)


# Runze Cheng / 05/Oct/2023
# Fizzbuzz

def Fizzbuzz():
    for i in range (1,101):
        if i%3 == 0:
            if i%5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

Fizzbuzz()
    
'''       
 String = ''
 String += 'Fizz'
 String += 'Buzz'
'''
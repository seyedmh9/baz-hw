import math
def fact(numbers):
    factorsNumbers = []
    for i in numbers:
        factorVar = str(i) + "! = " + str(math.factorial(i))
        factorsNumbers.append(factorVar)
    return factorsNumbers
        
N_number = int(input("Enter N number :"))
numbers = []
for i in range(N_number):
    numbers.append(int(input("Enter Number" + str(i + 1) + " :")))
Numandfact = fact(numbers)
for i in range(N_number):
    print(Numandfact[i])

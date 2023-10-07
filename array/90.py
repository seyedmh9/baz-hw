import math
N_number = int(input("Enter N number :"))
numbers = []
for i in range(N_number):
    numbers.append(int(input("Enter Number" + str(i + 1) + " :")))
fact = []

for i in numbers:
    fact.append(math.factorial(i))

for i in range(len(numbers)):
     print(str(numbers[i]) + "! = " + str(fact[i]))
import math
numbers = []
for i in range(3):
    numbers.append(int(input("Enter Number" + str(i + 1) + " :")))
numbers.sort()
print(numbers[len(numbers) - 1])

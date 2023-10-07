numbers = []
answer = []
for i in range(100):
    numbers.append(int(input("Enter Number" + str(i + 1) + " :")))
    if numbers[i] % 2 != 0:
        answer.append(int(numbers[i]))
fb1 = 0
fb2 = 1
fb3 = 0
for i in answer:
    while fb2 < i:
        fb3 = fb1 + fb3
        fb1 = fb2 
        fb2 = fb3
        if fb2 == i:
            print(i)

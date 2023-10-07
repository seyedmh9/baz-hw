numbers = []
for i in range(10):
    numbers.append(int(input("Enter Number" + str(i + 1) + " :")))
    
for i in numbers:
    checkAval = True
    for i2 in range(2,i):
        if i % i2 == 0:
            checkAval = False
            break
    if checkAval == False:
        print(i)

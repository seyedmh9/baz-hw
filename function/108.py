def aval(num):
    count = 0
    for i in num :
        check = True
        for i2 in range(2,i):
            if i % i2 == 0:
                check = False
                break
        if check == True and i != 1:
            count += 1
    return count

N_number = int(input("Enter N number :"))
number = []
for i in range(N_number):
    number.append(int(input("Enter Number" + str(i + 1) + " :")))
print(aval(number))
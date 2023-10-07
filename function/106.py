def zoj(num):
    count = 0
    for i in num:
        if i % 2 == 0 :
            count +=1
    return count

number = []
for i in range(5):
    number.append(int(input("Enter Number" + str(i + 1) + " :")))
print(zoj(number))
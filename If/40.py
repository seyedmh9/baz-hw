number1 = input("Enter number :")
number2 = input("Enter number :")
if len(number1) == len(number2) and len(number1) == 3:
    answer = bin(int(number1,2)+int(number2,2))[2:]
    print(answer)
else:
    print("Error!!")
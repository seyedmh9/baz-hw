javab = ''
number = input("Enter BinaryNumber :")
if len(number) == 4:
    for i in number:
        if i != "0":
            javab += i
    print(javab)
else:
    print("Error!!")
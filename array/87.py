N_number = int(input("Enter N number :"))
ArNum = []
for i in range(N_number):
    ArNum.append(int(input("Enter Number" + str(i + 1) + " :")))
ArNum.sort(reverse = True)
for i in ArNum:
    print(i)

N_number = int(input("Enter N number :"))
ArNum = []
ArCheck = []
for i in range(N_number):
    ArNum.append(int(input("Enter Number" + str(i + 1) + " :")))
ArCheck = ArNum
ArCheck = sorted(ArCheck)
count = 0
for i2 in range(N_number):
    if ArNum[i2] == ArCheck[i2]:
        count += 1
if count == N_number:
    print("Yes")
else:
    print("No")

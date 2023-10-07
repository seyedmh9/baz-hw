def sort_adad(number):
    number = sorted(number,reverse = True)
    return number

N_number = int(input("Enter N number :"))
numbers = []
for i in range(N_number):
    numbers.append(int(input("Enter Number" + str(i + 1) + " :")))

answer = sort_adad(numbers)
for i in answer:
    print(i)
0
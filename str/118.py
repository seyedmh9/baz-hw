Str_input = input("Enter a string :")
num = ""
for i in Str_input:
    if i.isdigit():
        num += i
print(num)
number = int(input("Enter a Number :"))
fb1 = 0
fb2 = 1
fb3 = 0
while fb2 < 99999:
    if fb2 % number == 0:
        print(fb2)
    fb3 = fb1 + fb2
    fb1 = fb2
    fb2 = fb3
    

for i in range(56,1985):
    for i2 in range(1,i + 1):
        if i % i2 == 0:
            print(f"{i} = {i2}")
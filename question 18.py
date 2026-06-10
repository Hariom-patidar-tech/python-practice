# Check if a number is Armstrong
num = 153
sum = 0
for i in num:
    if i // 10:
        if i ** 3:
            print("yes")
        else:
            print("no")
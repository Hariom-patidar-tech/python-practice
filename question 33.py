# Count numbers ending with 5

a = [23,3,15,32,98,85,65]
count = 0
for i in a:
    if i % 10 == 5:
        count += 1
print(count)
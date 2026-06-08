# Find sum of even numbers in a list
num = [12,22,11,31,44,8,6,90]
sum = 0
for i in num:
    if i % 2 == 0:
        sum += i
print(sum)
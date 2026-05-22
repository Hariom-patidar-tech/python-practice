#  find largest
num = [12,22,11,33,21,55,76]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print(largest)
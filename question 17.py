# Find largest odd number in a list
num = [12,2,4,6,33,11,98,88,44]
max_odd = None
for i in num:
    if i % 2 != 0:
        if max_odd is None or i > max_odd:
            max_odd = i
print("largest odd number:", max_odd)
        
        
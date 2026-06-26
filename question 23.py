# Find difference between max and min

numm = [11,22,33,44,99,88,77,66]
max_value = numm[0]
min_value = numm[0]
for num in numm:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num
        
diff = max_value - min_value
print(diff)
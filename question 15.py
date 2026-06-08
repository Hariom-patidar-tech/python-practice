# Find Smallest Even Number
num = [12,2,4,6,33,11,98,88,44]
min_even = num[0]
for i in num:
    if i % 2 == 0:
        if i < min_even:
            min_even = i
print("Smallest even number:", min_even)



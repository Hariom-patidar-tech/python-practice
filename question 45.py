# Find intersection of two lists (without using set)


l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

freq = {}

for num in l1:
    freq[num] = 1

result = []

for num in l2:
    if num in freq :
        result.append(num)

print(result)
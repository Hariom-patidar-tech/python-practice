# Find the sum of unique element only [1,1,2,2,3,4,5,5]

lst = [1,1,2,2,3,4,6,8,9,5,5]

freq = {}

for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

total = 0
for key in freq:
    if freq[key] == 1:
        total += key

print("Sum:", total)
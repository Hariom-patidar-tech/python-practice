# Find Element with Minimum Frquency

lst = [1,2,2,2,3,4,3,1,4,3,4]

freq = {}

for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

min_freq = float('inf')

for val in freq.values():
    if val < min_freq:
        min_freq = val

result = []
for key in freq:
    if freq[key] == min_freq:
        result.append(key)

print(result)


a = [1,2,2,2,2,2,3,3,3,3,4,4,4,]

freq = {}

for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

min_freq = float('inf')

for val in freq.values():
    if val < min_freq:
        min_freq = val

result = []
for key in freq:
    if freq[key] == min_freq:
        result.append(key)

print(result)
        
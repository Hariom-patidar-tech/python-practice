#Find all pairs whose sum = target

lst = [1,2,3,4,5]
target = 8

seen = set()
pairs = []

for num in lst:
    diff = target - num
    
    if diff in seen:
        pairs.append((diff, num))
    
    seen.add(num)

print(pairs)
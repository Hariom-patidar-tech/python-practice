

# Move all zeros to end

a = 12340007373077

a = list(map(int, str(a)))

b = 0

for i in range(len(a)):
    if a[i] != 0:
        a[b] = a[i]
        b += 1

for i in range(b, len(a)):
    a[i] = 0

print(a)
    
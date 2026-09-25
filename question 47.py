# Remove all invalid entries (None, negative, etc.)
lst = [1, None, -3, 4, 0, -2, 5]

clean = []

for num in lst:
    if num is not None:
        if num >= 0:
          clean.append(num)

print(clean)
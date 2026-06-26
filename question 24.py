# Remove all negative numbers from list

num = [11,22,-23,44,-33,-88]
new = []
for i in num:
    if i > 0:
        new.append(i)
print(new)
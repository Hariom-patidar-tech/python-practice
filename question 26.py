# Merge two lists without duplicates

a = [12,34,43,7,65,55]
b = [88,77,43,22,11]
merge = []
for i in a + b:
    if i not in merge:
        merge.append(i)
print(merge)

a = [12,34,43,7,65,55]
b = [88,77,43,22,11]
c = list(set((a+b)))
print(c)
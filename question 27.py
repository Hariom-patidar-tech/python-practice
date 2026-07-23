# Find common elements in two lists
a = [12,34,43,7,65,55]
b = [88,77,43,22,11]
common = []
for i in a:
    if i in b :
        common.append(i)
print(common)
    
    
    
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = [i for i in list1 if i in list2]
print(result)
# Remove Duplicates from List [1,2,3,4,3,2,2,4,5,7,9]

list = [1,2,3,4,3,2,2,4,5,7,9]
a = []
for i in list:
    if i not in  a:
        a.append(i)
print(a)
        
        
list2 = [1,2,3,4,3,2,2,4,5,7,9]

new_list = list(set(list2))
print(new_list)
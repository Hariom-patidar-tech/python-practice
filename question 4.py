# Find Second Largest Number in List


# a = [12,23,11,65,45,33]
# unique_lst = list(set(a))  
# unique_lst.sort()
# print("Second largest:", unique_lst[-2])


a = [12,23,11,65,45,33]
n = len(a)
largest = a[n-1]
second = 0
for num in a:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)
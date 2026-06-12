# Check if list is sorted or not


lst= [1,2,3,4,5]
is_sorted = True

for i in range(len(lst)-1):
    if lst[i] > lst[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Sorted")
else:
    print("Not Sorted")
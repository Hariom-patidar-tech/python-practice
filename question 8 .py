# Count Even and Odd Numbers in List
a = [11,22,2,4,33,17,88,89,76]
even = 0
odd = 0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
        
print("even",even)
print("odd",odd)
        
    
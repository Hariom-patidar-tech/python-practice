# Separate Even and Odd into Two Lists
num = [12,221,32,33,56,4,98,11]
even = []
odd = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even",even)
print("odd",odd)



# Replace Negative Numbers with 0
num = [1,22,-2,98,-66,62,-11]
for i in range(len(num)):
    if num[i] < 0:
        num[i] = 0
print(num)
        
        
        
num = [1,22,-2,98,-66,62,-11,55]
new_num = []
for i in num:
    if i < 0:
        new_num.append(0)
    else:
        new_num.append(i)
print(new_num)
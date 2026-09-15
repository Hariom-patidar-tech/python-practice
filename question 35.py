# Shift all 0 of the list to the end


a = 12300760045600876004567
b = 0

a = list(map(int,str(a)))

for i in range(len(a)):
    if a[i] != 0:
        a[b] = a[i]
        b += 1
        
for i in range(b,len(a)):
    a[i] = 0
    
print(a) 
# Check if Two Lists Are Rotations of Each Other

a = [11,12,13,14,15,16,17]
b = [15,16,17,11,12,13,14]

if len(a) != len(b):
    print("not rotate")
else:  
    temp = a + a
    found = False
    

    for i in range(len(a)):
        if temp[i:i+len(b)] == b:
            found = True
            break
    if found:
        print("rotate")
    else:
        print("Not rotate")
    
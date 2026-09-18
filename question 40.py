# Rotate List by position like [1,2,3,4,5,6] R=2 then [5,6,1,2,3,4]

lst = [1,2,3,4,5,6]
R = 2
rotated = lst[-R:] + lst[:-R]

print(rotated)





lst = [1,2,3,4,7,5,6]
R = 3

n = len(lst)
R = R % n

rotated = [0] * n

for i in range(n):
    new_index = (i + R) % n
    rotated[new_index] = lst[i]

print(rotated)
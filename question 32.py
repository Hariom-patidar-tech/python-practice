# Count Elements Equal to Average

a = [1,2,3,4,5]
sum = 0
count = 0
for i in a:
    sum += i
avg = sum / len(a)
for i in a:
    if i == avg:
        count += 1

print(avg)
print(count)


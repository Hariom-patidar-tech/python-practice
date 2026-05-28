# Count Positive and Negative Numbers - [1, -2, 3, -4, 5]
num = [1, -2, 3, -4, 5]
posi = []
neg = []
for i in num:
    if i > 0:
        posi.append(i)
    else:
        neg.append(i)
print("posi",posi)
print("negi",neg)
# Sum of Digits of a Number like 1234 are digts and sum is 1+2+3+4
sum = 0
for i in range(1,):
    sum += i
print(sum)




num = 12345
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print(sum)
    
    
# Find all prime numbers in a list
lst = [1,2, 3, 4, 5, 6, 7, 8, 9]

prime_list = []

for num in lst:
    if num > 1:
        is_prime = True
        
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_list.append(num)

print("Prime numbers:", prime_list)




# # Find all prime numbers in a list

lst = [2, 3, 4, 5, 6, 7, 8]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in lst if is_prime(num)]

print(primes)
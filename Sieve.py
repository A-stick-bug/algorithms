# Sieve of Eratosthenes for finding prime numbers

import time

start = time.time()

num = 60000
prime = [True for i in range(num + 1)]
# boolean array
p = 2
while p * p <= num:
    # If prime[p] is not changed, then it is a prime
    if prime[p]:
        # Updating all multiples of p
        for i in range(p * p, num + 1, p):
            prime[i] = False
    p += 1

end = time.time()
prime_list = []
for p in range(2, num + 1):
    if prime[p]:
        prime_list.append(p)

print(prime_list)
print(f"Prime numbers in list: {len(prime_list)}")
print(f"Time taken: {end - start} seconds")

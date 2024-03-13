def is_prime(x, ps):
    for p in ps:
        if x % p == 0:
            return False
    return True

def primes(n):
    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num, prime_list):
            prime_list.append(num)
    return prime_list

# Testen der Funktion
assert primes(1) == []
assert primes(3) == [2, 3]
assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
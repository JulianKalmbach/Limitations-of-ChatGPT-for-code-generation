def is_prime(x, ps):
    """Überprüft, ob x eine Primzahl ist, indem es auf Teilbarkeit durch die Zahlen in ps getestet wird."""
    for p in ps:
        if x % p == 0:
            return False
    return True

def primes(n):
    """Berechnet alle Primzahlen ≤ n."""
    prime_list = []
    for i in range(2, n+1):
        if is_prime(i, prime_list):
            prime_list.append(i)
    return prime_list

# Testen der Funktionen
assert primes(1) == []
assert primes(3) == [2, 3]
assert primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

primes(20)
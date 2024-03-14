import time

# Definition der originalen rekursiven Fibonacci-Funktion
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Dekorator für Caching
def cached(f):
    cache = {}
    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            result = f(n)
            cache[n] = result
            return result
    return wrapper

# Definition der dekorierten und optimierten Fibonacci-Funktion
@cached
def fib_fast_and_simple(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fast_and_simple(n-1) + fib_fast_and_simple(n-2)

# Messung der Ausführungszeit für fib(32)
start_time = time.time()
fib_32_result = fib(32)
fib_32_time = time.time() - start_time

# Messung der Ausführungszeit für fib_fast_and_simple(32)
start_time = time.time()
fib_fast_and_simple_32_result = fib_fast_and_simple(32)
fib_fast_and_simple_32_time = time.time() - start_time

(fib_32_result, fib_32_time, fib_fast_and_simple_32_result, fib_fast_and_simple_32_time)

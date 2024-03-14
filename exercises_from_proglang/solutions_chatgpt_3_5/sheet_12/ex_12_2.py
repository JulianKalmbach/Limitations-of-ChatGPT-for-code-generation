import time


def cached(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            result = func(n)
            cache[n] = result
            return result

    return wrapper


@cached
def fib_fast_and_simple(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_fast_and_simple(n - 1) + fib_fast_and_simple(n - 2)


def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# Measure execution time for fib(32)
start_time = time.time()
fib_result = fib(32)
end_time = time.time()
print("Execution time for fib(32):", end_time - start_time, "seconds")
print("fib(32) result:", fib_result)

# Measure execution time for fib_fast_and_simple(32)
start_time = time.time()
fib_fast_result = fib_fast_and_simple(32)
end_time = time.time()
print("Execution time for fib_fast_and_simple(32):", end_time - start_time, "seconds")
print("fib_fast_and_simple(32) result:", fib_fast_result)

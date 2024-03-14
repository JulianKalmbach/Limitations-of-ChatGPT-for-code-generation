from typing import Callable

def differentiate(f: Callable[[float], float], h: float = 1e-5) -> Callable[[float], float]:
    return lambda x0: (f(x0 + h) - f(x0 - h)) / (2 * h)

def newton(f: Callable[[float], float], x: float):
    while True:
        f_prime = differentiate(f)
        x = x - f(x) / f_prime(x)
        yield x

def generate_target(iterable, f: Callable[[float], float], target: float):
    for x in iterable:
        if abs(f(x)) < target:
            yield x
            break
        yield x

def arithmetic_mean(iterable):
    total = 0
    count = 0
    for x in iterable:
        count += 1
        total += x
        yield total / count

def map13(input_iterator):
    return map(lambda x: x % 13, input_iterator)

def filter57(input_iterator):
    return filter(lambda x: x % 5 == 0 or x % 7 == 0, input_iterator)

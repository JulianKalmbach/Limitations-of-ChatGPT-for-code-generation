from typing import Callable

def differentiate(f: Callable[[float], float], h: float) -> Callable[[float], float]:
    return lambda x0: (f(x0 + h) - f(x0 - h)) / (2 * h)

def newton(f: Callable[[float], float], x: float):
    f_prime = differentiate(f, 1e-10)
    while True:
        yield x - f(x) / f_prime(x)
        x = x - f(x) / f_prime(x)

generator = newton(lambda x: 2 * x + 1, 3)
for i in range(3):
    print(next(generator))

def generate_target(iterable, f, target):
    for value in iterable:
        yield value
        if abs(f(value)) < target:
            break

f = lambda x: 2 * x + 1
generator = newton(f, 3)
print(list(generate_target(generator, f, 1e-12)))

def arithmetic_mean(iterable):
    total = 0
    count = 0
    for value in iterable:
        total += value
        count += 1
        yield total / count

print(list(arithmetic_mean(iter(range(0, 21, 4)))))

def map13(iterable):
    return map(lambda x: x % 13, iterable)

input_iterator = iter(range(0, 26, 5))
assert list(map13(input_iterator)) == [0, 5, 10, 2, 7, 12]

def filter57(iterable):
    return filter(lambda x: x % 5 == 0 or x % 7 == 0, iterable)

input_iterator = iter(range(20))
assert list(filter57(input_iterator)) == [0, 5, 7, 10, 14, 15]

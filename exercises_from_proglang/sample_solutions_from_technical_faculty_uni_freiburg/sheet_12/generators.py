from typing import Callable, Iterator


def differentiate(f: Callable[[float], float],
                  h: float) -> Callable[[float], float]:
    return lambda x0: (f(x0 + h) - f(x0 - h)) / (2 * h)


# (a)
def newton(f: Callable[[float], float], x: float) -> Iterator[float]:
    xn = x
    while True:
        xn = xn - f(xn) / differentiate(f, 1e-5)(xn)
        yield xn


# (b)
def generate_target(iterable: Iterator,
                    f: Callable[[float], float],
                    target: float) -> Iterator:
    for x in iterable:
        yield x
        if abs(f(x)) < target:
            break


# (c)
def arithmetic_mean(iterable: Iterator) -> Iterator[float]:
    current_sum = 0

    for i, x in enumerate(iterable, start=1):
        current_sum += x

        yield current_sum / i


# (d)
def map13(iterable: Iterator[int]) -> Iterator[int]:
    return map(lambda x: x % 13, iterable)


# (e)
def filter57(iterable: Iterator[int]) -> Iterator[int]:
    return filter(lambda x: x % 5 == 0 or x % 7 == 0, iterable)

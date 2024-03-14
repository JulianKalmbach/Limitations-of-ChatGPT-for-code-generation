import math

from pytest import approx
from typing import Callable


def differentiate(f: Callable[[float], float],
                  h: float) -> Callable[[float], float]:
    return lambda x0: (f(x0 + h) - f(x0 - h)) / (2 * h)


def integrate(f: Callable[[float], float],
              n: int) -> Callable[[float, float], float]:
    def simpson(a: float, b: float) -> float:
        # More functional but not covered by the lecture yet.
        # h = (b - a) / n
        # return sum(h / 6
        #            * (f(a + i * h)
        #               + 4 * f((a + i * h + a + (i + 1) * h) / 2)
        #               + f(a + (i + 1) * h))
        #            for i in range(n))

        tmp_sum = 0
        h = (b - a) / n
        for i in range(n):
            xi = a + i * h
            xii = a + (i + 1) * h
            si = h / 6 * (f(xi) + 4 * f((xi + xii) / 2) + f(xii))
            tmp_sum += si

        return tmp_sum

    return simpson


if __name__ == "__main__":
    assert approx(2.0) == differentiate(lambda x: 2 * x, 0.5)(0)
    assert approx(1.0) == differentiate(lambda x: 1 / 2 * x ** 2, 1e-2)(1)
    assert approx(math.e, rel=1e-2) == differentiate(
        lambda x: math.exp(x), 0.1)(1)

    assert approx(74.1481) == integrate(lambda x: 3 ** (3 * x - 1), 3)(0, 2)
    assert approx(1.0) == integrate(lambda x: 2 * x, 5)(0, 1)
    assert approx(math.e - 1) == integrate(lambda x: math.exp(x), 5)(0, 1)

from random import randint
from typing import Callable


def polynom_n(p: list[int]) -> Callable[[int], int]:
    def f(x: int) -> int:
        result = 0
        for a in reversed(p):
            result = x * result + a
        return result
    return f


def test_one_cracker_n(n: int, cracker_n):
    p = []
    for _ in range(n + 1):
        p = p + [randint(-100, 100)]
    print("checking", p)
    c = cracker_n(polynom_n(p))
    assert c == p, f"failed for polynomial {p} found {c}"


def test_many_cracker_n(n: int, cracker_n):
    for _ in range(1000):
        test_one_cracker_n(n, cracker_n)
    print("Passed 1000 tests")

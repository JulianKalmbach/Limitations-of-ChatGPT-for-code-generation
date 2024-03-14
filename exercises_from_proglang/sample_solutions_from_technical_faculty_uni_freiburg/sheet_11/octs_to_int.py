from functools import reduce
from typing import Callable


octs_to_int: Callable[[list[int]], int] = lambda octs: reduce(
    lambda n, b: n * 8 + b, octs, 0)

if __name__ == "__main__":
    assert octs_to_int([6, 4, 4]) == 420

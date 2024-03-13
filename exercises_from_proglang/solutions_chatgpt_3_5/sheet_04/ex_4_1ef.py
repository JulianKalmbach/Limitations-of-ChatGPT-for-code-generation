def average(numbers):
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

from math import isclose

eps = 1e-4
assert isclose(average([]), 0.0, abs_tol=eps, rel_tol=eps)
assert isclose(average([1.0]), 1.0, rel_tol=eps)
assert isclose(average([5.0, 10.0, 15.0, 20.0]), 12.5, rel_tol=eps)
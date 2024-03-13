def calculate_pi(n):
    if n <= 0:
        return 0.0

    pi_squared_over_6 = sum(1 / i ** 2 for i in range(1, n + 1))
    pi = (pi_squared_over_6 * 6) ** 0.5
    return pi

from math import isclose

eps = 1e-4
assert isclose(calculate_pi(-3), 0.0, abs_tol=eps, rel_tol=eps)
assert isclose(calculate_pi(1), 2.44948, rel_tol=eps)
assert isclose(calculate_pi(7), 3.01177, rel_tol=eps)
assert isclose(calculate_pi(1000), 3.14063, rel_tol=eps)
assert isclose(calculate_pi(10000), 3.14149, rel_tol=eps)
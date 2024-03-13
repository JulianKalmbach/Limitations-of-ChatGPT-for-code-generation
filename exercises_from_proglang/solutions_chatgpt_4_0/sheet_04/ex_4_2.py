def calculate_pi(n):
    if n < 1:
        return 0.0
    sum_series = sum(1 / i**2 for i in range(1, n + 1))
    pi_approx = (sum_series * 6) ** 0.5
    return pi_approx

# Testing the function as specified
from math import isclose

eps=1e-4
# Test cases
test_results = [
    isclose(calculate_pi(-3), 0.0, abs_tol=eps, rel_tol=eps),
    isclose(calculate_pi(1), 2.44948, rel_tol=eps),
    isclose(calculate_pi(7), 3.01177, rel_tol=eps),
    isclose(calculate_pi(1000), 3.14063, rel_tol=eps),
    isclose(calculate_pi(10000), 3.14149, rel_tol=eps)
]

test_results
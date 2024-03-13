from math import isclose


def calculate_pi(n: int) -> float:
    acc = 0.0
    for i in range(n):
        acc += 1 / (i + 1) ** 2
    return (acc * 6) ** 0.5


if __name__ == "__main__":
    eps = 1e-4
    assert isclose(calculate_pi(-3), 0.0, abs_tol = eps, rel_tol = eps)
    assert isclose(calculate_pi(1), 2.44948, rel_tol = eps)
    assert isclose(calculate_pi(7), 3.01177, rel_tol = eps)
    assert isclose(calculate_pi(1000), 3.14063, rel_tol = eps)
    assert isclose(calculate_pi(10000), 3.14149, rel_tol = eps)

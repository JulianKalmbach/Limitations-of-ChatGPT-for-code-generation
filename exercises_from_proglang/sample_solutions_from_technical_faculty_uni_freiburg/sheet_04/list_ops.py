from math import isclose


def average(xs: list[float]) -> float:
    if len(xs) == 0:
        return 0.0
    else:
        acc = 0.0
        for x in xs:
            acc = acc + x
        return acc / len(xs)


def reverse(xs: list) -> list:
    ys = []
    for x in xs:
        ys = [x] + ys
    return ys


def only_positive(xs: list[int]) -> list[int]:
    ys = []
    for x in xs:
        if x > 0:
            ys = ys + [x]
    return ys


if __name__ == "__main__":
    eps = 1e-4
    assert isclose(average([]), 0.0, abs_tol = eps, rel_tol = eps)
    assert isclose(average([1.0]), 1.0, rel_tol = eps)
    assert isclose(average([5.0, 10.0, 15.0, 20.0]), 12.5, rel_tol = eps)

    assert reverse([]) == []
    assert reverse([1, 2, 3]) == [3, 2, 1]
    assert reverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    assert only_positive([]) == []
    assert only_positive([1, 2, 3]) == [1, 2, 3]
    assert only_positive([-8, 1, -5, -9, 2, -7, 3, -6, 0]) == [1, 2, 3]

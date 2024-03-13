def crack_1(f):
    # Initialisierung der Koeffizienten
    a_0 = f(0)
    a_1 = f(1) - a_0

    return [a_0, a_1]


# Test
def f10(x: int) -> int:
    return 1 + 2 * x


def f11(x: int) -> int:
    return -1 + 3 * x


assert crack_1(f10) == [1, 2]
assert crack_1(f11) == [-1, 3]


def crack_2(f):
    # Initialisierung der Koeffizienten
    a_0 = f(0)
    a_1 = (f(1) - f(0)) - a_0
    a_2 = f(2) - f(1) - a_1 - a_0

    return [a_0, a_1, a_2]


# Test
def f20(x: int) -> int:
    return 1 + 2 * x + x * x


def f21(x: int) -> int:
    return -1 - 4 * x + 2 * x * x


def f22(x: int) -> int:
    return (x + 1) * (x - 1)


assert crack_2(f20) == [1, 2, 1]
assert crack_2(f21) == [-1, -4, 2]
assert crack_2(f22) == [-1, 0, 1]


def crack_3(f):
    # Initialisierung der Koeffizienten
    a_0 = f(0)
    a_1 = (f(1) - f(0)) - a_0
    a_2 = (f(2) - f(1)) - (f(1) - f(0)) - a_1 - a_0
    a_3 = f(3) - f(2) - (f(2) - f(1)) - f(1) + f(0) - a_2 - a_1 - a_0

    return [a_0, a_1, a_2, a_3]


# Test
def f30(x: int) -> int:
    return x * (x + 10) * (x - 5)


assert crack_3(f30) == [0, -50, 5, 1]

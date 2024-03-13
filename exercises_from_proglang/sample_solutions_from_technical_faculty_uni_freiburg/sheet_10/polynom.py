def f10(x: int) -> int:
    return 1 + 2 * x


def f11(x: int) -> int:
    return -1 + 3 * x


def crack_1(f) -> list[int]:
    a0 = f(0)
    a1 = f(1) - a0
    return [a0, a1]


def f20(x: int) -> int:
    return 1 + 2 * x + x * x


def f21(x: int) -> int:
    return -1 - 4 * x + 2 * x * x


def f22(x: int) -> int:
    return(x + 1) * (x - 1)


def crack_2(f) -> list[int]:
    a0 = f(0)
    a1_a2 = f(1) - f(0)
    a1x2_a2x4 = f(2) - f(0)
    a2 = (a1x2_a2x4 - 2 * a1_a2) // 2
    a1 = a1_a2 - a2
    return [a0, a1, a2]


def f30(x: int) -> int:
    return x * (x + 10) * (x - 5)


def crack_3(f) -> list[int]:
    f0 = f(0)  # a0
    f1 = f(1)  # a0 + a1 + a2 + a3
    f2 = f(2)  # a0 + 2 a1 + 4 a2 + 8 a3
    f3 = f(3)  # a0 + 3 a1 + 9 a2 + 27 a3

    df0 = f1 - f0  # a1 + a2 + a3
    df1 = f2 - f1  # a1 + 3 a2 + 7 a3
    df2 = f3 - f2  # a1 + 5 a2 + 19 a3

    ddf0 = df1 - df0  # 2 a2 + 6 a3
    ddf1 = df2 - df1  # 2 a2 + 12 a3

    dddf0 = ddf1 - ddf0  # 6 a3

    a3 = dddf0 // 6
    a2 = (ddf0 - dddf0) // 2
    a1 = df0 - a2 - a3
    a0 = f0

    return [a0, a1, a2, a3]


if __name__ == "__main__":
    assert crack_1(f10) == [1, 2]
    assert crack_1(f11) == [-1, 3]

    assert crack_2(f20) == [1, 2, 1]
    assert crack_2(f21) == [-1, -4, 2]
    assert crack_2(f22) == [-1, 0, 1]

    assert crack_3(f30) == [0, -50, 5, 1]

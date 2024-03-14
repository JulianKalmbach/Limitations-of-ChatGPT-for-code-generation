my_filter = lambda xs, ys: set(filter(lambda x: x not in ys, xs))

my_diff = lambda xs, ys: my_filter(xs, ys) | my_filter(ys, xs)

if __name__ == "__main__":
    a = {1, 2, 3}
    b = {3, 4, 5}
    assert my_filter(a, b) == {1, 2}
    assert my_filter(b, a) == {4, 5}

    assert my_diff(a, b) == {1, 2, 4, 5}

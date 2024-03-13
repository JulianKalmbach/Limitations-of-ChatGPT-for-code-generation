from vector import Vector, apply_binary_operator


def test_vector():
    # create vectors
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])
    v3 = Vector([2, 4, 8])

    # test properties
    assert v1.dimension == 3
    assert v1.len - 3.74165738 < 1e-6
    for a, b in zip(v1.values, [1, 2, 3]):
        assert a == b

    # test str representation
    assert str(v1) == "3D vector: [1, 2, 3]"

    # test unary operators
    assert v1 == v2
    assert v1 != v3

    # test helper function
    assert apply_binary_operator("+", 5, 3) == 8
    assert apply_binary_operator("-", 5, 3) == 2
    assert apply_binary_operator("*", 5, 3) == 15

    # test binary operators
    assert +v1 == Vector([1, 2, 3])
    assert -v1 == Vector([-1, -2, -3])
    assert v1 + v2 == Vector([2, 4, 6])
    assert v1 + 1 == Vector([2, 3, 4])
    assert 1 + v1 == Vector([2, 3, 4])
    assert v1 - v2 == Vector([0, 0, 0])
    assert 1 - v1 == Vector([0, -1, -2])
    assert v1 * v2 == Vector([1, 4, 9])
    assert v1 * 4 == Vector([4, 8, 12])
    assert 4 * v1 == Vector([4, 8, 12])
    assert (v1 * 2.5 - Vector([2.5, 5, 7.5])).len < 1e-8


if __name__ == "__main__":
    test_vector()

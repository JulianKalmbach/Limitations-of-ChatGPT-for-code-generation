inc = lambda x: x + 1
mul = lambda x, y: x * y

compose = lambda f, g: lambda x, y: f(g(x, y))

if __name__ == "__main__":
    assert compose(inc, mul)(4, 2) == 9

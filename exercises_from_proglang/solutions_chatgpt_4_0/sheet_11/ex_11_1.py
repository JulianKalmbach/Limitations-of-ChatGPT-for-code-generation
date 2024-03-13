def compose(f, g):
    return lambda x, y: f(g(x, y))

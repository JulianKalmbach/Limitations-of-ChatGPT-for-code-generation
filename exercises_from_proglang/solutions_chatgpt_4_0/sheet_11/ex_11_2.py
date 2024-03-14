def my_filter(xs, ys):
    return xs - ys

def my_diff(xs, ys):
    return my_filter(xs, ys) | my_filter(ys, xs)

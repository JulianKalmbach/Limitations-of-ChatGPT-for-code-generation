my_filter = lambda xs, ys: xs - ys

my_diff = lambda xs, ys: my_filter(xs, ys) | my_filter(ys, xs)

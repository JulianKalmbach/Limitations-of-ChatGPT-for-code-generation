from turtle import forward, right, pendown, penup, Screen, speed, left


def sierpinski_g(size: int, n: int):
    """Helper for Sierpiński implementing G-rule."""

    if n == 0:
        forward(size)
    else:
        sierpinski_g(size, n - 1)  # G
        sierpinski_g(size, n - 1)  # G


def sierpinski_f(size: int, n: int):
    """Helper for Sierpiński implementing F-rule."""

    if n == 0:
        forward(size)
    else:
        sierpinski_f(size, n - 1)  # F
        right(120)                 # -
        sierpinski_g(size, n - 1)  # G
        left(120)                  # +
        sierpinski_f(size, n - 1)  # F
        left(120)                  # +
        sierpinski_g(size, n - 1)  # G
        right(120)                 # -
        sierpinski_f(size, n - 1)  # F


def sierpinski(size: int, n: int):
    """Draw n generations of the Sierpiński triangle of size n.

    Args:
        size: The size of a side of the smallest triangle.
        n:    The number of generations to draw.

    Returns:
        None.

    """
    pendown()
    sierpinski_f(size, n)  # F
    right(120)             # -
    sierpinski_g(size, n)  # G
    right(120)             # -
    sierpinski_g(size, n)  # G
    penup()


if __name__ == '__main__':
    # Draw the Sierpiński triangle.
    screen = Screen()
    speed(0)
    sierpinski(10, 5)
    screen.exitonclick()

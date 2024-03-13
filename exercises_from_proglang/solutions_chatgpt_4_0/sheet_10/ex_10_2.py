import turtle


def apply_rules(ch):
    if ch == 'F':
        return 'F-G+F+G-F'
    elif ch == 'G':
        return 'GG'
    else:
        return ch


def process_string(old_str):
    new_str = ""
    for ch in old_str:
        new_str += apply_rules(ch)
    return new_str


def create_l_system(iters, axiom):
    start_string = axiom
    end_string = ""
    for i in range(iters):
        end_string = process_string(start_string)
        start_string = end_string
    return end_string


def draw_l_system(turtle, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F' or cmd == 'G':
            turtle.forward(distance)
        elif cmd == '+':
            turtle.left(angle)
        elif cmd == '-':
            turtle.right(angle)


def sierpinski(size, n):
    turtle.setup(800, 800)
    window = turtle.Screen()
    window.title("Sierpinski Triangle")

    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.goto(-200, -150)
    t.down()

    t.color("black")
    instructions = create_l_system(n, "F-G-G")
    draw_l_system(t, instructions, 120, size)

    window.mainloop()


# Beispielaufruf für n=2 und Streckenlänge 10
sierpinski(10, 2)

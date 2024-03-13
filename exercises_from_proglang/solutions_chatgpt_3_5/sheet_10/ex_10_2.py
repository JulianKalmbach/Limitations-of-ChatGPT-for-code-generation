import turtle

def apply_rule(symbol):
    if symbol == 'F':
        return 'F−G−G'
    elif symbol == 'G':
        return 'GG'
    else:
        return symbol

def generate_string(axiom, rules, iterations):
    for _ in range(iterations):
        axiom = ''.join([rules.get(c, c) for c in axiom])
    return axiom

def draw_sierpinski(size, n):
    axiom = 'F−G−G'
    rules = {'F': 'F−G+F+G−F', 'G': 'GG'}
    string = generate_string(axiom, rules, n)

    turtle.speed(0)
    turtle.up()
    turtle.setpos(-size * 1.5 / 2, -size / 2)
    turtle.down()

    stack = []

    for char in string:
        if char == 'F' or char == 'G':
            turtle.forward(size)
        elif char == '+':
            turtle.left(120)
        elif char == '-':
            turtle.right(120)
        elif char == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif char == ']':
            position, heading = stack.pop()
            turtle.up()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.down()

    turtle.hideturtle()
    turtle.done()

# Beispielaufruf
draw_sierpinski(100, 2)

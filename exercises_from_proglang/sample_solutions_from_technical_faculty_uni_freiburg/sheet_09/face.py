from math import pi

from geo import GuiWrapper, Vector2D
from shapes import Circle, RotatableEllipse, Triangle


def main():
    gui = GuiWrapper(width=800, height=600)

    RotatableEllipse(Vector2D(300, 200), Vector2D(70, 30), pi / 12).draw(
        gui, fillcolor="")
    Circle(Vector2D(300, 200), 20).draw(gui, fillcolor="lightblue")
    Circle(Vector2D(300, 200), 5).draw(gui, fillcolor="black")
    Triangle(Vector2D(220, 130), Vector2D(0, 20), Vector2D(130, 10)).draw(
        gui, fillcolor="black")

    RotatableEllipse(Vector2D(500, 200), Vector2D(70, 30), 11 * pi / 12).draw(
        gui, fillcolor="")
    Circle(Vector2D(500, 200), 20).draw(gui, fillcolor="lightblue")
    Circle(Vector2D(500, 200), 5).draw(gui, fillcolor="black")

    Triangle(Vector2D(580, 130), Vector2D(0, 20), Vector2D(-130, 10)).draw(
        gui, fillcolor="black")

    RotatableEllipse(Vector2D(400, 300), Vector2D(20, 70), 0).draw(
        gui, fillcolor="pink")

    Triangle(Vector2D(250, 400), Vector2D(300, 0), Vector2D(150, 100)).draw(
        gui, fillcolor="", outlinecolor="black")

    gui.start()


if __name__ == "__main__":
    main()

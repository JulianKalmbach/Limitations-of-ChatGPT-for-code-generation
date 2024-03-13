from dataclasses import dataclass
from math import pi, sin, cos

from geo import Object2D, GuiWrapper, Vector2D


@dataclass
class Circle(Object2D):
    """
    A circle in 2D space.

    Invariants:
        radius > 0
    """
    __radius: float

    @property
    def radius(self) -> float:
        return self.__radius

    @property
    def top_left(self) -> Vector2D:
        return self.__top_left

    @property
    def bottom_right(self) -> Vector2D:
        return self.__bottom_right

    def __post_init__(self):
        assert self.__radius > 0, (
            f"radius must be greater than 0 but is {self.__radius}")
        self.__top_left = self.pos - Vector2D(self.__radius, self.__radius)
        self.__bottom_right = self.pos + Vector2D(self.__radius, self.__radius)

    def draw(self, gui: GuiWrapper, fillcolor: str = "black",
             outlinecolor: str = "black"):
        gui.canvas.create_oval(self.top_left.x, self.top_left.y,
                               self.bottom_right.x, self.bottom_right.y,
                               fill=fillcolor, outline=outlinecolor)


@dataclass
class RotatableEllipse(Object2D):
    """
    An ellipse in 2D space that can be rotated.

    Invariants:
        size.x > 0
        size.y > 0
        0 <= angle < 2 * pi
    """
    __size: Vector2D
    __angle: float

    @property
    def size(self) -> Vector2D:
        return self.__size

    @property
    def angle(self) -> float:
        return self.__angle

    def __post_init__(self):
        assert self.__size.x > 0, (
            f"size.x must be greater than 0 but is {self.__size.x}")
        assert self.__size.y > 0, (
            f"size.y must be greater than 0 but is {self.__size.y}")
        assert 0 <= self.__angle < 2 * pi, (
            f"angle must be between 0 and 2 * pi but is {self.__angle}")

    def draw(self, gui: GuiWrapper, fillcolor: str = "black",
             outlinecolor: str = "black"):
        # create list of points that defines the ellipse
        points = []
        num_points = 360
        for i in range(0, num_points):
            rad = i * (2 * pi / num_points)
            # get distance from center for unrotated ellipse
            dx = self.__size.x * cos(rad)
            dy = self.__size.y * sin(rad)
            # rotate dx and dy by angle
            rdx = + dx * cos(self.__angle) + dy * sin(self.__angle)
            rdy = - dx * sin(self.__angle) + dy * cos(self.__angle)
            # offset by center to get the final point
            x = self.pos.x + rdx
            y = self.pos.y + rdy
            # add flattened coordinates to point list
            points.extend((x, y))
        # draw the rotated ellipse
        gui.canvas.create_polygon(*points, fill=fillcolor,
                                  outline=outlinecolor)


@dataclass
class Triangle(Object2D):
    """
    A triangle in 2D
    """
    __edge1: Vector2D
    __edge2: Vector2D

    @property
    def edge1(self) -> Vector2D:
        return self.__edge1

    @property
    def edge2(self) -> Vector2D:
        return self.__edge2

    @property
    def abs_edge1(self) -> Vector2D:
        return self.pos + self.__edge1

    @property
    def abs_edge2(self) -> Vector2D:
        return self.pos + self.__edge2

    def draw(self, gui: GuiWrapper, fillcolor: str = "black",
             outlinecolor: str = "black"):
        # triangle is a polygon consisting of 3 points
        gui.canvas.create_polygon(
            self.pos.x, self.pos.y,
            self.abs_edge1.x, self.abs_edge1.y,
            self.abs_edge2.x, self.abs_edge2.y,
            fill=fillcolor, outline=outlinecolor)


def main():
    gui = GuiWrapper(width=800, height=600)

    circle = Circle(Vector2D(100, 200), 75)
    circle.draw(gui, fillcolor="lightblue")

    ellipse = RotatableEllipse(Vector2D(300, 250), Vector2D(200, 50),
                               7 * pi / 5)
    ellipse.draw(gui, fillcolor="pink")

    triangle = Triangle(Vector2D(450, 150), Vector2D(200, 150),
                        Vector2D(100, 350))
    triangle.draw(gui, fillcolor="green", outlinecolor="black")

    gui.start()


if __name__ == "__main__":
    main()

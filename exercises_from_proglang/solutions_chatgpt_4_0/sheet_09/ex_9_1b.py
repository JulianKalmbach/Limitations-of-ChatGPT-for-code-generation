from dataclasses import dataclass, field
from math import cos, sin, pi
from exercises_from_proglang.sample_solutions_from_technical_faculty_uni_freiburg.sheet_09.geo import Object2D, Vector2D, GuiWrapper # import adjusted. Originally was: from geo import Object2D, Vector2D, GuiWrapper


@dataclass
class RotatableEllipse(Object2D):
    size: Vector2D
    angle: float
    __points: list[float] = field(init=False, repr=False)

    def __post_init__(self):
        if self.size.x <= 0 or self.size.y <= 0:
            raise ValueError("Size dimensions must be greater than 0")
        if not (0 <= self.angle < 2 * pi):
            raise ValueError("Angle must be in the range [0, 2π)")
        self.__calculate_ellipse_points()

    def __calculate_ellipse_points(self):
        self.__points = []
        for degree in range(360):
            rad = degree * pi / 180
            x = self.size.x * cos(rad)
            y = self.size.y * sin(rad)
            # Rotate point
            rotated_x = x * cos(self.angle) - y * sin(self.angle)
            rotated_y = x * sin(self.angle) + y * cos(self.angle)
            # Translate point to position
            self.__points.append(rotated_x + self.pos.x)
            self.__points.append(rotated_y + self.pos.y)

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        gui.canvas.create_polygon(*self.__points, fill=fillcolor, outline=outlinecolor)

# Test code
if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    ellipse = RotatableEllipse(Vector2D(300, 250), Vector2D(200, 50), 7 * pi / 5)
    ellipse.draw(gui, fillcolor="pink")
    gui.start()

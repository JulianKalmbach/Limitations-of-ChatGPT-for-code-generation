from math import cos, sin, pi
from exercises_from_proglang.sample_solutions_from_technical_faculty_uni_freiburg.sheet_09.geo import Object2D, Vector2D, GuiWrapper # import adjusted to fit the data structure. Origianlly was: from geo import Object2D, Vector2D, GuiWrapper


class RotatableEllipse(Object2D):
    def __init__(self, pos: Vector2D, size: Vector2D, angle: float):
        super().__init__(pos)
        self._size = size
        self._angle = angle

    @property
    def size(self) -> Vector2D:
        return self._size

    @property
    def angle(self) -> float:
        return self._angle

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        num_points = 360
        points = []
        for i in range(num_points):
            x = self.pos.x + self.size.x * cos(i * 2 * pi / num_points)
            y = self.pos.y + self.size.y * sin(i * 2 * pi / num_points)
            rotated_x = (x - self.pos.x) * cos(self.angle) - (y - self.pos.y) * sin(self.angle) + self.pos.x
            rotated_y = (x - self.pos.x) * sin(self.angle) + (y - self.pos.y) * cos(self.angle) + self.pos.y
            points.extend([rotated_x, rotated_y])
        gui.canvas.create_polygon(*points, fill=fillcolor, outline=outlinecolor)


if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    ellipse = RotatableEllipse(Vector2D(300, 250), Vector2D(200, 50), 7 * pi / 5)
    ellipse.draw(gui, fillcolor="pink")
    gui.start()

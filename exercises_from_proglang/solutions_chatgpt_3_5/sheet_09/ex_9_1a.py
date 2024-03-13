from exercises_from_proglang.sample_solutions_from_technical_faculty_uni_freiburg.sheet_09.geo import Object2D, Vector2D, GuiWrapper # import adjusted to fit the data structure. Origianlly was: from geo import Object2D, Vector2D, GuiWrapper


class Circle(Object2D):
    def __init__(self, pos: Vector2D, radius: float):
        super().__init__(pos)
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def top_left(self) -> Vector2D:
        return Vector2D(self.pos.x - self.radius, self.pos.y - self.radius)

    @property
    def bottom_right(self) -> Vector2D:
        return Vector2D(self.pos.x + self.radius, self.pos.y + self.radius)

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        top_left = self.top_left
        bottom_right = self.bottom_right
        gui.canvas.create_oval(top_left.x, top_left.y, bottom_right.x, bottom_right.y,
                               fill=fillcolor, outline=outlinecolor)


if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    circle = Circle(Vector2D(100, 200), 75)
    circle.draw(gui, fillcolor="lightblue")
    gui.start()
from dataclasses import field, dataclass # this import was missing
from exercises_from_proglang.sample_solutions_from_technical_faculty_uni_freiburg.sheet_09.geo import Object2D, Vector2D, GuiWrapper # import adjusted. Originally was: from geo import Object2D, Vector2D, GuiWrapper


@dataclass
class Circle(Object2D):
    _radius: float
    __top_left: Vector2D = field(init=False)
    __bottom_right: Vector2D = field(init=False)

    def __post_init__(self):
        if self._radius <= 0:
            raise ValueError("Radius must be greater than 0")
        self.__calculate_bounds()

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def top_left(self) -> Vector2D:
        return self.__top_left

    @property
    def bottom_right(self) -> Vector2D:
        return self.__bottom_right

    def __calculate_bounds(self):
        self.__top_left = Vector2D(self.pos.x - self.radius, self.pos.y - self.radius)
        self.__bottom_right = Vector2D(self.pos.x + self.radius, self.pos.y + self.radius)

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        gui.canvas.create_oval(self.top_left.x, self.top_left.y,
                               self.bottom_right.x, self.bottom_right.y,
                               fill=fillcolor, outline=outlinecolor)

# Test code
if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    circle = Circle(Vector2D(100, 200), 75)
    circle.draw(gui, fillcolor="lightblue")
    gui.start()

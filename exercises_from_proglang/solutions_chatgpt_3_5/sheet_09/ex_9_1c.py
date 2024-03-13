from exercises_from_proglang.sample_solutions_from_technical_faculty_uni_freiburg.sheet_09.geo import Object2D, Vector2D, GuiWrapper # import adjusted to fit the data structure. Origianlly was: from geo import Object2D, Vector2D, GuiWrapper


class Triangle(Object2D):
    def __init__(self, pos: Vector2D, edge1: Vector2D, edge2: Vector2D):
        super().__init__(pos)
        self._edge1 = edge1
        self._edge2 = edge2

    @property
    def edge1(self) -> Vector2D:
        return self._edge1

    @property
    def edge2(self) -> Vector2D:
        return self._edge2

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        points = [self.pos.x, self.pos.y, self.edge1.x, self.edge1.y, self.edge2.x, self.edge2.y]
        gui.canvas.create_polygon(*points, fill=fillcolor, outline=outlinecolor)


if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    triangle = Triangle(Vector2D(450, 150), Vector2D(200, 150), Vector2D(100, 350))
    triangle.draw(gui, fillcolor="green", outlinecolor="black")
    gui.start()

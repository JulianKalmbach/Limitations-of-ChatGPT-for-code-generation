from dataclasses import dataclass
from exercises_from_proglang.sample_solutions_from_technical_faculty_uni_freiburg.sheet_09.geo import Object2D, Vector2D, GuiWrapper # import adjusted. Originally was: from geo import Object2D, Vector2D, GuiWrapper


@dataclass
class Triangle(Object2D):
    edge1: Vector2D
    edge2: Vector2D

    def draw(self, gui: GuiWrapper, fillcolor: str = "black", outlinecolor: str = "black"):
        # Erste Ecke ist die Position des Dreiecks
        first_corner = (self.pos.x, self.pos.y)
        # Die anderen Ecken werden relativ zur ersten Ecke positioniert
        second_corner = (self.pos.x + self.edge1.x, self.pos.y + self.edge1.y)
        third_corner = (self.pos.x + self.edge2.x, self.pos.y + self.edge2.y)

        # Zeichnen des Dreiecks mit den berechneten Ecken
        gui.canvas.create_polygon(first_corner, second_corner, third_corner,
                                  fill=fillcolor, outline=outlinecolor)

# Beispielcode zum Testen des Dreiecks
if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    triangle = Triangle(Vector2D(450, 150), Vector2D(200, 150), Vector2D(100, 350))
    triangle.draw(gui, fillcolor="green", outlinecolor="black")
    gui.start()

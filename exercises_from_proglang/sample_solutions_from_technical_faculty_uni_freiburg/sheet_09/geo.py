from __future__ import annotations

import abc
import tkinter as tk
from dataclasses import dataclass, field


@dataclass
class GuiWrapper:
    width: int
    height: int
    root: tk.Tk = field(init=False, repr=False)
    canvas: tk.Canvas = field(init=False, repr=False)

    def __post_init__(self):
        self.root = tk.Tk()
        self.root.title("Geometry")
        self.root.geometry(f"{self.width}x{self.height}")
        self.canvas = tk.Canvas(self.root,
                                width=self.width, height=self.height)
        self.canvas.pack()

    def start(self):
        self.root.mainloop()


@dataclass
class Vector2D:
    x: float
    y: float

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)


@dataclass
class Object2D(metaclass=abc.ABCMeta):
    __pos: Vector2D

    @property
    def pos(self) -> Vector2D:
        return self.__pos

    @abc.abstractmethod
    def draw(self, gui: GuiWrapper, fillcolor: str = "black",
             outlinecolor: str = "black"):
        pass

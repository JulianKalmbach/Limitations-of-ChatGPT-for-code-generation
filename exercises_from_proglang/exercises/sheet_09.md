### 9.1
Betrachten Sie die vorgegebene Datei geo.py.
Sie hat den Inhalt:
````python
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
````
- GuiWrapper ist eine Datenklasse, die ein Fenster mit einer Zeichenfläche öffnet. Dafür wird das Standardmodul tkinter verwendet.
- Vector2D beschreibt einen 2-dimensionalen Vektor. Beachten sie die Operator-Überladung: ein solcher Vektor kann 
negiert (-), zwei Vektoren können addiert (+) oder subtrahiert (-) werden.
- Object2D beschreibt schließlich ein zu zeichnendes Objekt mit einer Position. 

Die Methode draw ist mithilfe des Pakets 
abc als sogenannte “abstrakte Methode” deklariert, die von abgeleiteten Klassen implementiert werden muss. Damit dies 
zur Laufzeit überprüft wird, wird die Klasse mit metaclass=abc.ABCMeta deklariert und die Methode mit 
@abc.abstractmethod dekoriert.

#### a)
Erstellen Sie die Datenklasse Circle nach den folgenden Vorgaben. Importieren Sie die benötigten Datenklassen aus der 
Datei geo.py. Beachten Sie die in der Vorlesung beschriebenen Regeln für Invarianten und Properties. 
Insbesondere sollen alle Properties read-only sein.

- Superklasse ist Object2D.
- Zusätzlich zur Position (Mittelpunkt) aus Object2D hat der Kreis einen Radius > 0. Definieren Sie den Radius als 
Property namens radius und stellen Sie sicher, dass die Invariante nicht verletzt wird.
- Erstellen Sie zusätzlich die beiden Properties top_left und bottom_right, diese sind vom Typ Vector2D und beschreiben
die Eckpunkte des klein-sten umschließenden Quadrats. Diese Properties sollen einmalig aus Radius und Position 
berechnet werden.
- Implementieren Sie die Methode draw, verwenden Sie hierfür
gui.canvas.create_oval. Diese Methode benötigt 4 Koordinaten für die zwei Eckpunkte sowie die Farbwerte mit den 
keywords fill und outline.

Testen Sie die Implementierung wie folgt. Beachten Sie die Reihenfolge der Aufrufe: Zunächst wird das GUI erstellt, 
dann werden alle Objekte erstellt und gezeichnet, danach wird das GUI gestartet.

````python
if __name__ == "__main__":
    gui = GuiWrapper(width=800, height=600)
    circle = Circle(Vector2D(100, 200), 75)
    circle.draw(gui, fillcolor="lightblue")
    gui.start()
````

#### b)
Erstellen Sie die Datenklasse RotatableEllipse wie folgt:
- Superklasse ist Object2D.
- Zusätzlich zur Position (Mittelpunkt) aus Object2D hat die Ellipse die folgenden Properties: size definiert den 
horizontalen und vertikalen Radius der Ellipse, d.h. die halbe Breite und Höhe. Der Typ ist Vector2D, beide Koordinaten 
müssen größer als 0 sein. angle definiert den Winkel der Ellipse im Bogenmaß. Die Ellipse wird gegen den Uhrzeigersinn 
um den Mittelpunkt rotiert. Der Typ ist float, der Wert muss innerhalb des Intervalls von 0 (eingeschlossen) bis 2π 
(ausgeschlossen) liegen.
- Implementieren Sie die Methode draw, verwenden Sie hierfür
gui.canvas.create_polygon. Erstellen Sie eine Liste mit 360 Punkten [x1, y1, ..., x360, y360], um die Ellipse zu 
beschreiben. Verwenden Sie den star-operator *liste um die Koordinaten der Punkte der Funk-tion zu übergeben. Dieser 
Operator wandelt die Liste in einzelne Argumente um. Beispiel: funktion(*[1, 2, 3]) entspricht funktion(1, 2, 3). 
Übergeben Sie die Farbwerte mit den keywords fill und outline.
- Eine Lösungsmöglichkeit besteht darin, die Punkte der Ellipse jeweils um den Nullpunkt zu berechnen, danach um den 
Nullpunkt zu drehen und dann zu verschieben.

Zeichnen Sie die Ellipse wie folgt:
````python
ellipse = RotatableEllipse(Vector2D(300, 250), Vector2D(200, 50),
7 * pi / 5)
ellipse.draw(gui, fillcolor="pink")
````

#### c)
Schlussendlich erstellen Sie noch die Datenklasse Triangle:
- Superklasse ist Object2D.
- Zusätzlich zur Position (eine Ecke des Dreiecks) aus Object2D hat das Dreieck die Properties edge1 und edge2 um die 
relative Position der bei-den anderen Ecken zu beschreiben.
- Zeichnen Sie das Dreieck mit gui.canvas.create_polygon. Übergeben Sie die Farbwerte mit den keywords fill und outline.

Zeichnen Sie das Dreieck wie folgt:
````python
triangle = Triangle(Vector2D(450, 150), Vector2D(200, 150), Vector2D(100, 350))
triangle.draw(gui, fillcolor="green", outlinecolor="black")
````

### 9.3
Implementieren Sie die Datenklasse Vector, welche einen Vektor von reellen Zahlen mit beliebiger Dimension abbilden kann.
- Repräsentieren Sie reelle Zahlen durch den Typ float.
- Vektorinstanzen sollen unveränderlich sein, zum Ändern eines Wertes muss eine neue Instanz erzeugt werden.
- Für Invarianten und Properties gelten die selben Regeln wie in der ersten Auf-gabe des Blattes.

#### a)
Erstellen Sie zunächst die Hilfsfunktion apply_binary_operator. Diese Funk-tion soll einen String für den Operator und 
zwei reelle Zahlen als Argumente nehmen. Je nach Operator ("+", "-" oder "*") soll die entsprechende Berechnung 
ausgeführt und das Ergebnis zurückgegeben werden. Bei fehlerhaftem Operator soll ein ValueError erzeugt werden. 
Verwenden Sie Pattern Matching. Verwenden Sie insbesondere nicht eval.

```
>>> print(apply_binary_operator("-", 5, 3))
2
```

#### b)
Erstellen Sie die Datenklasse Vector mit den folgenden Eigenschaften:
- Property values, eine Liste reeller Zahlen, die den Vektor beschreibt.
- Properties dimension (Dimension des Vektors) und len (Euklidische Län-ge des Vektors). Diese Properties sollen 
einmalig automatisch berechnet werden. Die Dimension muss größer als 0 sein.
- Definiere die Methode \_\_str__ zur Umwandlung des Vektors in einen String: print(Vector([1, 2, 3])) soll ausgegeben 
werden als 3D vector:[1, 2, 3].
- Definiere Methoden zum Überladen der folgenden unären Operatoren: \_\_pos__ (+) gibt den Vektor selbst zurück. 
\_\_neg__ (-) wendet Negation auf jedes Element an.
- Methode operate_binary: Diese nimmt einen String für den Operator und ein weiteres Argument other und berechnet das 
Ergebnis der Operation mit der obigen Hilfsfunktion. other kann ein Vektor oder eine reelle Zahl (d.h., int oder float) 
sein. Im Falle eines Vektors soll sichergestellt werden, dass beide Vektoren die selbe Dimension haben. Anschließend 
soll die Berechnung elementweise durchgeführt werden. Im Falle einer reellen Zahl soll die Berechnung zwischen jedem 
dem Element des Vektors und der Zahl durchgeführt werden. Der Rückgabewert ist in beiden Fällen ein neuer Vektor. Für 
alle anderen Eingaben soll ein TypeError erzeugt werden.
- Definiere Methoden zum Überladen der folgenden binären Operatoren: \_\_add__ (+), \_\_sub__ (-), und \_\_mul__ (*). 
Es soll jeweils die Methode operate_binary aufgerufen werden.
- Definiere Methoden zum Überladen der Operatoren, wenn ein Skalar links und der Vektor rechts steht, in der selben 
Weise wie zuvor: \_\_radd__ (+), \_\_rsub__ (-) und \_\_rmul__ (*).

Testen Sie Ihre Implementierung mit der Datei test_vector.py.

Diese hat den folgenden Inhalt:
````python
from vector import Vector, apply_binary_operator


def test_vector():
    # create vectors
    v1 = Vector([1, 2, 3])
    v2 = Vector([1, 2, 3])
    v3 = Vector([2, 4, 8])

    # test properties
    assert v1.dimension == 3
    assert v1.len - 3.74165738 < 1e-6
    for a, b in zip(v1.values, [1, 2, 3]):
        assert a == b

    # test str representation
    assert str(v1) == "3D vector: [1, 2, 3]"

    # test unary operators
    assert v1 == v2
    assert v1 != v3

    # test helper function
    assert apply_binary_operator("+", 5, 3) == 8
    assert apply_binary_operator("-", 5, 3) == 2
    assert apply_binary_operator("*", 5, 3) == 15

    # test binary operators
    assert +v1 == Vector([1, 2, 3])
    assert -v1 == Vector([-1, -2, -3])
    assert v1 + v2 == Vector([2, 4, 6])
    assert v1 + 1 == Vector([2, 3, 4])
    assert 1 + v1 == Vector([2, 3, 4])
    assert v1 - v2 == Vector([0, 0, 0])
    assert 1 - v1 == Vector([0, -1, -2])
    assert v1 * v2 == Vector([1, 4, 9])
    assert v1 * 4 == Vector([4, 8, 12])
    assert 4 * v1 == Vector([4, 8, 12])
    assert (v1 * 2.5 - Vector([2.5, 5, 7.5])).len < 1e-8


if __name__ == "__main__":
    test_vector()
````

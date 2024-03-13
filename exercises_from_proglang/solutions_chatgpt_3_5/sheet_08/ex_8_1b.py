from dataclasses import dataclass

@dataclass
class Fahrzeug:
    zustand: int
    neupreis: int
    leergewicht: int
    baujahr: int

    def __post_init__(self):
        assert 0 <= self.zustand <= 100, f"Zustand {self.zustand}% muss zwischen 0% und 100% liegen."
        assert self.neupreis >= 0, f"Neupreis {self.neupreis}€ muss mindestens 0€ sein."
        assert self.leergewicht > 0, f"Leergewicht {self.leergewicht}kg muss größer als 0kg sein."
        assert self.baujahr > 1900, f"Baujahr {self.baujahr} muss größer als 1900 sein."

@dataclass
class Kraftfahrzeug(Fahrzeug):
    leistung: int
    sitzplaetze: int

    def __post_init__(self):
        super().__post_init__()
        assert self.leistung > 0, f"Leistung {self.leistung}kW muss größer als 0kW sein."
        assert self.sitzplaetze > 0, f"Sitzplätze {self.sitzplaetze} muss größer als 0 sein."

@dataclass
class Bus(Kraftfahrzeug):
    stehplaetze: int

    def __post_init__(self):
        super().__post_init__()
        assert 0 <= self.stehplaetze <= self.sitzplaetze, f"Stehplätze {self.stehplaetze} muss kleiner oder gleich Sitzplätze {self.sitzplaetze} sein."

@dataclass
class PKW(Kraftfahrzeug):
    pass

@dataclass
class LKW(Kraftfahrzeug):
    zuladung: int

    def __post_init__(self):
        super().__post_init__()
        assert self.zuladung > 0, f"Zuladung {self.zuladung}kg muss größer als 0kg sein."
        assert self.zuladung <= self.leergewicht * 2, f"Zuladung {self.zuladung}kg muss größer als 0kg und maximal {self.leergewicht * 2}kg sein."

@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

    def __post_init__(self):
        super().__post_init__()
        assert self.rahmengroesse > 0, f"Rahmengröße {self.rahmengroesse}cm muss größer als 0cm sein."

# Test the classes
try:
    print(Bus(-7, 100000, 2500, 1995, 200, 80, 40))
except AssertionError as e:
    print(e)

try:
    print(Bus(25, -12, 2500, 1995, 200, 80, 40))
except AssertionError as e:
    print(e)

try:
    print(Bus(25, 100000, -3, 1995, 200, 80, 40))
except AssertionError as e:
    print(e)

try:
    print(Bus(25, 100000, 2500, 1800, 200, 80, 40))
except AssertionError as e:
    print(e)

try:
    print(Bus(25, 100000, 2500, 1995, -42, 80, 40))
except AssertionError as e:
    print(e)

try:
    print(Bus(25, 100000, 2500, 1995, 200, -80, 40))
except AssertionError as e:
    print(e)

try:
    print(Bus(25, 100000, 2500, 1995, 200, 40, 80))
except AssertionError as e:
    print(e)

try:
    print(Fahrrad(100, 500, 10, 2019, -55))
except AssertionError as e:
    print(e)

try:
    print(LKW(65, 150000, 3200, 1991, 280, 3, 46000))
except AssertionError as e:
    print(e)
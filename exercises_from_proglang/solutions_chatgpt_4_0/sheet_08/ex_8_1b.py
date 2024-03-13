from dataclasses import dataclass, field

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
    leistung: int = field(init=False)

    def __post_init__(self):
        super().__post_init__()
        assert self.leistung > 0, f"Leistung {self.leistung}kW muss größer als 0kW sein."

@dataclass
class Bus(Kraftfahrzeug):
    sitzplaetze: int
    stehplaetze: int

    def __post_init__(self):
        super().__post_init__()
        assert self.sitzplaetze > 0, f"Sitzplätze {self.sitzplaetze} muss größer als 0 sein."
        assert self.stehplaetze <= self.sitzplaetze, f"Stehplätze {self.stehplaetze} muss kleiner oder gleich Sitzplätze {self.sitzplaetze} sein."

@dataclass
class PKW(Kraftfahrzeug):
    sitzplaetze: int

    def __post_init__(self):
        super().__post_init__()
        assert self.sitzplaetze > 0, f"Sitzplätze {self.sitzplaetze} muss größer als 0 sein."

@dataclass
class LKW(Kraftfahrzeug):
    sitzplaetze: int
    zuladung: int

    def __post_init__(self):
        super().__post_init__()
        assert self.sitzplaetze > 0, f"Sitzplätze {self.sitzplaetze} muss größer als 0 sein."
        assert 0 < self.zuladung <= 2 * self.leergewicht, f"Zuladung {self.zuladung}kg muss größer als 0kg und maximal {2 * self.leergewicht}kg sein."

@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

    def __post_init__(self):
        super().__post_init__()
        assert self.rahmengroesse > 0, f"Rahmengröße {self.rahmengroesse}cm muss größer als 0cm sein."
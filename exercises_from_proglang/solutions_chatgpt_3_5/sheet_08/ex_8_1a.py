from dataclasses import dataclass

@dataclass
class Fahrzeug:
    zustand: int
    neupreis: int
    leergewicht: int
    baujahr: int

@dataclass
class Kraftfahrzeug(Fahrzeug):
    leistung: int
    sitzplaetze: int

@dataclass
class Bus(Kraftfahrzeug):
    stehplaetze: int

@dataclass
class PKW(Kraftfahrzeug):
    pass

@dataclass
class LKW(Kraftfahrzeug):
    zuladung: int

@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

# Test the classes
print(Bus(25, 100000, 2500, 1995, 200, 80, 40))
print(Fahrrad(100, 500, 10, 2019, 55))
print(PKW(95, 20000, 1200, 2016, 90, 5))
print(LKW(65, 150000, 3200, 1991, 280, 3, 4600))
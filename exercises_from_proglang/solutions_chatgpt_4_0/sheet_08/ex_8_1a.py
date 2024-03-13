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

@dataclass
class Bus(Kraftfahrzeug):
    sitzplaetze: int
    stehplaetze: int

@dataclass
class PKW(Kraftfahrzeug):
    sitzplaetze: int

@dataclass
class LKW(Kraftfahrzeug):
    sitzplaetze: int
    zuladung: int

@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

# Überprüfung der Klassen
bus = Bus(25, 100000, 2500, 1995, 200, 80, 40)
fahrrad = Fahrrad(100, 500, 10, 2019, 55)
pkw = PKW(95, 20000, 1200, 2016, 90, 5)
lkw = LKW(65, 150000, 3200, 1991, 280, 3, 4600)

print(bus)
print(fahrrad)
print(pkw)
print(lkw)
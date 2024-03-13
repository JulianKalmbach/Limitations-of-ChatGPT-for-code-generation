from dataclasses import dataclass
import math

@dataclass
class Fahrzeug:
    zustand: int
    neupreis: int
    leergewicht: int
    baujahr: int

    def gewicht(self) -> int:
        return self.leergewicht

    def alter(self) -> int:
        current_year = 2022
        if self.baujahr > current_year:
            return 0
        return current_year - self.baujahr

    def marktwert(self) -> int:
        alter = self.alter()
        zustand = self.zustand - 5 * alter
        marktwert = zustand * self.neupreis / 100
        if marktwert < 0:
            marktwert = 0
        return int(marktwert)

    def maut(self) -> int:
        raise NotImplementedError("Diese Methode muss in den Subklassen überschrieben werden.")

@dataclass
class Kraftfahrzeug(Fahrzeug):
    leistung: int
    sitzplaetze: int

    def plaetze(self) -> int:
        return self.sitzplaetze

@dataclass
class Bus(Kraftfahrzeug):
    stehplaetze: int

    def plaetze(self) -> int:
        return self.sitzplaetze + self.stehplaetze

    def maut(self) -> int:
        maut_preis = (self.gewicht() / 5) + (self.plaetze() * 25)
        return int(maut_preis)

@dataclass
class PKW(Kraftfahrzeug):
    def maut(self) -> int:
        maut_preis = (self.gewicht() / 5) + (self.plaetze() * 25)
        return int(maut_preis)

    def marktwert(self) -> int:
        marktwert = super().marktwert()
        marktwert *= 0.5  # Rabatt von 50% auf Fahrräder
        return marktwert

@dataclass
class LKW(Kraftfahrzeug):
    zuladung: int

    def gewicht(self) -> int:
        return self.leergewicht + self.zuladung

    def maut(self) -> int:
        maut_preis = (self.gewicht() / 5) + (self.plaetze() * 25)
        maut_preis *= 2  # Doppelte Maut für LKWs
        return int(maut_preis)

@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

    def maut(self) -> int:
        return 0

# Test the classes
bus = Bus(25, 100000, 2500, 1995, 200, 80, 40)
print("Maut:", bus.maut())

pkw = PKW(95, 20000, 1200, 2016, 90, 5)
print("Alter:", pkw.alter(), "Marktwert:", pkw.marktwert())
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Fahrzeug:
    zustand: int
    neupreis: int
    leergewicht: int
    baujahr: int

    def gewicht(self) -> int:
        return self.leergewicht

    def maut(self) -> int:
        raise NotImplementedError

    def alter(self) -> int:
        aktuelles_jahr = datetime.now().year
        return max(0, aktuelles_jahr - self.baujahr)

    def marktwert(self) -> int:
        prozentwert = self.zustand - 5 * self.alter()
        marktwert = prozentwert / 100 * self.neupreis
        return max(0, marktwert)

@dataclass
class Kraftfahrzeug(Fahrzeug):
    leistung: int

    def plaetze(self) -> int:
        raise NotImplementedError

    def maut(self) -> int:
        return int((self.gewicht() / 5) + (25 * self.plaetze()))

@dataclass
class Bus(Kraftfahrzeug):
    sitzplaetze: int
    stehplaetze: int

    def plaetze(self) -> int:
        return self.sitzplaetze + self.stehplaetze

@dataclass
class PKW(Kraftfahrzeug):
    sitzplaetze: int

    def plaetze(self) -> int:
        return self.sitzplaetze

@dataclass
class LKW(Kraftfahrzeug):
    sitzplaetze: int
    zuladung: int

    def plaetze(self) -> int:
        return self.sitzplaetze

    def maut(self) -> int:
        return super().maut() * 2

@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

    def maut(self) -> int:
        return 0

    def marktwert(self) -> int:
        marktwert = super().marktwert()
        return int(marktwert * 0.5)

# Beispiele zur Überprüfung der Implementierung
bus = Bus(25, 100000, 2500, 1995, 200, 80, 40)
print("Maut:", bus.maut()) # Beispieloutput für Bus

pkw = PKW(95, 20000, 1200, 2016, 90, 5)
print("Alter:", pkw.alter(), "Marktwert:", pkw.marktwert()) # Beispieloutput für PKW
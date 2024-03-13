from dataclasses import dataclass


@dataclass
class Fahrzeug:
    zustand: int
    neupreis: int
    leergewicht: int
    baujahr: int

    def __post_init__(self):
        assert 0 <= self.zustand <= 100, f"Zustand " + str(
            self.zustand) + "% muss zwischen 0% und 100% liegen."
        assert self.neupreis >= 0, f"Neupreis " + str(
            self.neupreis) + "€ muss mindestens 0€ sein."
        assert self.leergewicht > 0, f"Leergewicht " + str(
            self.leergewicht) + "kg muss größer als 0kg sein."
        assert self.baujahr > 1900, f"Baujahr " + str(
            self.baujahr) + " muss größer als 1900 sein."

    def gewicht(self) -> int:
        return self.leergewicht

    def maut(self) -> int:
        raise NotImplementedError

    def alter(self) -> int:
        return max(2022 - self.baujahr, 0)

    def marktwert(self) -> int:
        return max(self.neupreis * (self.zustand - 5 * self.alter()) // 100, 0)


@dataclass
class Kraftfahrzeug(Fahrzeug):
    leistung: int
    sitzplaetze: int

    def __post_init__(self):
        super().__post_init__()
        assert self.leistung > 0, f"Leistung " + str(
            self.leistung) + "kW muss größer als 0kW sein."
        assert self.sitzplaetze > 0, f"Sitzplätze " + str(
            self.sitzplaetze) + " muss größer als 0 sein."

    def plaetze(self) -> int:
        return self.sitzplaetze

    def maut(self) -> int:
        return self.gewicht() // 5 + self.plaetze() * 25


@dataclass
class Bus(Kraftfahrzeug):
    stehplaetze: int

    def __post_init__(self):
        super().__post_init__()
        assert self.stehplaetze <= self.sitzplaetze, f"Stehplätze " + str(
            self.stehplaetze) + " muss kleiner oder gleich Sitzplätze " + str(
            self.sitzplaetze) + " sein."

    def plaetze(self) -> int:
        return super().plaetze() + self.stehplaetze


@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

    def __post_init__(self):
        super().__post_init__()
        assert self.rahmengroesse > 0, f"Rahmengröße " + str(
            self.rahmengroesse) + "cm muss größer als 0cm sein."

    def maut(self) -> int:
        return 0

    def marktwert(self) -> int:
        return super().marktwert() * 50 // 100


@dataclass
class PKW(Kraftfahrzeug):
    pass


@dataclass
class LKW(Kraftfahrzeug):
    zuladung: int

    def __post_init__(self):
        super().__post_init__()
        max_zuladung = 2 * self.leergewicht
        assert 0 < self.zuladung <= max_zuladung, f"Zuladung " + str(
            self.zuladung) + "kg muss größer als 0kg und maximal " + str(
            max_zuladung) + "kg sein."

    def gewicht(self) -> int:
        return super().gewicht() + self.zuladung

    def maut(self) -> int:
        return super().maut() * 2


def main():
    # Erstellung, Ausgabe und asserts
    print(Fahrzeug(55, 1000, 1, 2120))
    print(Kraftfahrzeug(65, 5000, 300, 1901, 2020, 1))
    print(Bus(25, 100000, 2500, 1995, 200, 80, 40))
    print(Fahrrad(100, 500, 10, 2019, 55))
    print(PKW(95, 20000, 1200, 2016, 90, 5))
    print(LKW(65, 150000, 3200, 1991, 280, 3, 4600))

    # Mautberechnung
    bus = Bus(25, 100000, 2500, 1995, 200, 80, 40)
    print("Maut:", bus.maut())

    # Marktwertberechnung
    pkw = PKW(95, 20000, 1200, 2016, 90, 5)
    print("Alter:", pkw.alter(), "Marktwert:", pkw.marktwert())

    # # Fehlerhafte Definitionen zur Überprüfung der asserts
    # Bus(-7, 100000, 2500, 1995, 200, 80, 40)
    # Bus(25, -12, 2500, 1995, 200, 80, 40)
    # Bus(25, 100000, -3, 1995, 200, 80, 40)
    # Bus(25, 100000, 2500, 1800, 200, 80, 40)
    # Bus(25, 100000, 2500, 1995, -42, 80, 40)
    # Bus(25, 100000, 2500, 1995, 200, -80, 40)
    # Bus(25, 100000, 2500, 1995, 200, 40, 80)
    # Fahrrad(100, 500, 10, 2019, -55)
    # LKW(65, 150000, 3200, 1991, 280, 3, 46000)


if __name__ == "__main__":
    main()

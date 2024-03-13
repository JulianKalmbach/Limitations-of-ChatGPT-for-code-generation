import math

def berechne_mantelflaeche(radius, hoehe):
    # Berechnung der Seitenlänge des Kegels
    s = math.sqrt(radius ** 2 + hoehe ** 2)
    # Berechnung der Mantelfläche
    mantelflaeche = math.pi * radius * s
    return mantelflaeche

def main():
    # Benutzereingabe für Radius und Höhe
    radius = float(input("Radius: "))
    hoehe = float(input("Höhe: "))
    # Berechnung der Mantelfläche
    mantelflaeche = berechne_mantelflaeche(radius, hoehe)
    # Ausgabe der Mantelfläche, gerundet auf zwei Nachkommastellen
    print(f"Mantelfläche: {mantelflaeche:.2f}")

if __name__ == "__main__":
    main()
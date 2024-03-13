def main():
    # Benutzer zur Eingabe einer Fließkommazahl auffordern
    kommazahl = float(input("Bitte geben Sie eine beliebige Fließkommazahl ein: "))

    # Quadrieren der eingegebenen Zahl
    quadriert = kommazahl ** 2
    print("Kommazahl:", kommazahl)
    print("Quadriert:", quadriert)

    # Methode 1: Quadrierte Zahl mit int() abrunden
    abgerundet_methode1 = int(quadriert)
    print("Methode 1:", abgerundet_methode1)

    # Methode 2: Quadrierte Zahl mit round() abrunden
    abgerundet_methode2 = round(quadriert)
    print("Methode 2:", abgerundet_methode2)

    # Methode 3: Quadrierte Zahl mit math.floor() abrunden
    import math
    abgerundet_methode3 = math.floor(quadriert)
    print("Methode 3:", abgerundet_methode3)

if __name__ == "__main__":
    main()
# Benutzer zur Eingabe einer Fließkommazahl auffordern
kommazahl = float(input("Kommazahl: "))

# Die Zahl quadrieren
quadriert = kommazahl ** 2
print("Quadriert:", quadriert)

# Methode 1: Abrunden mit int()
methode1 = int(quadriert)
print("Methode 1:", float(methode1))

# Methode 2: Abrunden mit der round()-Funktion (ohne Dezimalstellen)
methode2 = round(quadriert)
print("Methode 2:", methode2)

# Methode 3: Abrunden durch Subtraktion des Restwerts der Division durch 1
methode3 = quadriert - (quadriert % 1)
print("Methode 3:", methode3)
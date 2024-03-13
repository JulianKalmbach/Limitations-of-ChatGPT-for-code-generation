z = float(input("Kommazahl: "))
q = z ** 2
print("Quadriert:", str(q))

e1 = float(int(q))
print("Methode 1:", str(e1))

e2 = q // 1
print("Methode 2:", str(e2))

e3 = q - q % 1
print("Methode 3:", str(e3))

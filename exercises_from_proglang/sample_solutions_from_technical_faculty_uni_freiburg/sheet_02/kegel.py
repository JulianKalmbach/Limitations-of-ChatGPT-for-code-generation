pi = 3.14159
r = float(input("Radius: "))
h = float(input("Höhe: "))
s = (r ** 2 + h ** 2) ** 0.5
m = r * pi * s
print("Mantelfläche:", round(m, 2))

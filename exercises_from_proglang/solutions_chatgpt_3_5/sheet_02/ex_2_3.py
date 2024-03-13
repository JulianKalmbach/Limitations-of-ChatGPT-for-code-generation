import math

def main():
    radius = float(input("Radius eingeben: "))
    höhe = float(input("Höhe eingeben: "))

    mantelfläche = calculate_mantelfläche(radius, höhe)

    print(f"Radius: {radius}")
    print(f"Höhe: {höhe}")
    print(f"Mantelfläche: {mantelfläche:.2f}")

def calculate_mantelfläche(radius, höhe):
    mantelfläche = math.pi * radius * math.sqrt(radius ** 2 + höhe ** 2)
    return mantelfläche

if __name__ == "__main__":
    main()
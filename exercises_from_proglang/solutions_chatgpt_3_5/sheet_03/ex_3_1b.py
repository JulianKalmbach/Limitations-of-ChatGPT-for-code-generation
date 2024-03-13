from ex_3_1a import cone_area #adjusted import to fit the names of the exercises chatgpt originally generated: from cone_area_lib import cone_area

def main():
    # Werte für den Kegel festlegen
    radius = float(input("Radius: "))
    height = float(input("Höhe: "))

    # Mantelfläche berechnen
    surface_area = cone_area(radius, height)

    # Ergebnis ausgeben
    print(f"Mantelfläche: {surface_area:.2f}")

if __name__ == "__main__":
    main()
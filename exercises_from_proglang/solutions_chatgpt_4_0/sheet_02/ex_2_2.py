def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def main():
    # Eingabe des Benutzers entgegennehmen
    celsius = float(input("Bitte geben Sie die Temperatur in Celsius ein: "))

    # Umrechnung in Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)

    # Ausgabe des gerundeten Werts
    print(f"Celsius: {celsius} Fahrenheit: {round(fahrenheit, 2)}")

if __name__ == "__main__":
    main()
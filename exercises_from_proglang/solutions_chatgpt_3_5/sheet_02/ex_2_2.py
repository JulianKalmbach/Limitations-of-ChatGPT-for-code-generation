def main():
    celsius = float(input("Bitte geben Sie den Celsius-Wert ein: "))
    fahrenheit = celsius * 9/5 + 32
    fahrenheit_rounded = round(fahrenheit, 2)
    print(f"Celsius: {celsius} Fahrenheit: {fahrenheit_rounded}")

if __name__ == "__main__":
    main()
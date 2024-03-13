def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

if __name__ == "__main__":
    source_unit = input("Enter source unit [C / F / K]: ")
    source_value = float(input("Enter source value: "))
    target_unit = input("Enter target unit [C / F / K]: ")

    if source_unit == "C":
        if target_unit == "F":
            print(f"{source_value} C corresponds to {celsius_to_fahrenheit(source_value)} F.")
        elif target_unit == "K":
            print(f"{source_value} C corresponds to {celsius_to_kelvin(source_value)} K.")
    elif source_unit == "F":
        if target_unit == "C":
            print(f"{source_value} F corresponds to {fahrenheit_to_celsius(source_value)} C.")
        elif target_unit == "K":
            print(f"{source_value} F corresponds to {fahrenheit_to_kelvin(source_value)} K.")
    elif source_unit == "K":
        if target_unit == "C":
            print(f"{source_value} K corresponds to {kelvin_to_celsius(source_value)} C.")
        elif target_unit == "F":
            print(f"{source_value} K corresponds to {kelvin_to_fahrenheit(source_value)} F.")
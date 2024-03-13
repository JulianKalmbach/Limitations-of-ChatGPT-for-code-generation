def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

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

    if source_unit == 'C':
        if target_unit == 'F':
            result = celsius_to_fahrenheit(source_value)
            print(f"{source_value} C corresponds to {result} F.")
        elif target_unit == 'K':
            result = celsius_to_kelvin(source_value)
            print(f"{source_value} C corresponds to {result} K.")
        else:
            print("Invalid target unit.")
    elif source_unit == 'F':
        if target_unit == 'C':
            result = fahrenheit_to_celsius(source_value)
            print(f"{source_value} F corresponds to {result} C.")
        elif target_unit == 'K':
            result = fahrenheit_to_kelvin(source_value)
            print(f"{source_value} F corresponds to {result} K.")
        else:
            print("Invalid target unit.")
    elif source_unit == 'K':
        if target_unit == 'C':
            result = kelvin_to_celsius(source_value)
            print(f"{source_value} K corresponds to {result} C.")
        elif target_unit == 'F':
            result = kelvin_to_fahrenheit(source_value)
            print(f"{source_value} K corresponds to {result} F.")
        else:
            print("Invalid target unit.")
    else:
        print("Invalid source unit.")
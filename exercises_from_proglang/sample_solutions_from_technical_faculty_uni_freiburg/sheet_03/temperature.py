def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15 

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15 

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

if __name__ == '__main__':
    source_unit = input("Enter source unit [C / F / K]: ")
    source_val = float(input("Enter source value: "))
    target_unit = input("Enter target unit [C / F / K]: ")

    if source_unit == target_unit:
        target_val = source_val
    elif source_unit == "C" and target_unit == "F":
        target_val = celsius_to_fahrenheit(source_val)
    elif source_unit == "C" and target_unit == "K":
        target_val = celsius_to_kelvin(source_val)
    elif source_unit == "F" and target_unit == "C":
        target_val = fahrenheit_to_celsius(source_val)
    elif source_unit == "F" and target_unit == "K":
        target_val = fahrenheit_to_kelvin(source_val)
    elif source_unit == "K" and target_unit == "C":
        target_val = kelvin_to_celsius(source_val)
    elif source_unit == "K" and target_unit == "F":
        target_val = kelvin_to_fahrenheit(source_val)

    print("")
    print(source_val, source_unit, "corresponds to", target_val, target_unit + ".")


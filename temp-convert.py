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

conversion_functions = {
    1: celsius_to_fahrenheit,
    2: fahrenheit_to_celsius,
    3: kelvin_to_celsius,
    4: celsius_to_kelvin,
    5: fahrenheit_to_kelvin,
    6: kelvin_to_fahrenheit
}

print("Welcome to Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Kelvin to Celsius")
print("4. Celsius to Kelvin")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice: "))
if choice in conversion_functions:
    temperature = float(input("Enter temperature: "))
    converted_temperature = conversion_functions[choice](temperature)
    print("Converted temperature:", converted_temperature)
else:
    print("Invalid choice")

print("Thank you for using this temperature converter.")    


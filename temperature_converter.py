
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return (kelvin * 9/5) - 459.67

def main():
    print("Temperature Conversion Program")
    print("-------------------------------")
    try:
        temperature = float(input("Enter The Temperature Value: "))
        original_unit = input("Enter The Original Unit [Celsius, Fahrenheit, or Kelvin]: ").lower()

        if original_unit == "celsius":
            fahrenheit = celsius_to_fahrenheit(temperature)
            kelvin = celsius_to_kelvin(temperature)
            print(f"\nConverted Temperatures:")
            print(f"Celsius: {temperature:.2f} °C")
            print(f"Fahrenheit: {fahrenheit:.2f} °F")
            print(f"Kelvin: {kelvin:.2f} K")
        elif original_unit == "fahrenheit":
            celsius = fahrenheit_to_celsius(temperature)
            kelvin = fahrenheit_to_kelvin(temperature)
            print(f"\nConverted Temperatures:")
            print(f"Celsius: {celsius:.2f} °C")
            print(f"Fahrenheit: {temperature:.2f} °F")
            print(f"Kelvin: {kelvin:.2f} K")
        elif original_unit == "kelvin":
            celsius = kelvin_to_celsius(temperature)
            fahrenheit = kelvin_to_fahrenheit(temperature)
            print(f"\nConverted Temperatures:")
            print(f"Celsius: {celsius:.2f} °C")
            print(f"Fahrenheit: {fahrenheit:.2f} °F")
            print(f"Kelvin: {temperature:.2f} K")
        else:
            print("Invalid Input. Please Enter Celsius, Fahrenheit, or Kelvin.")

    except ValueError:
        print("Invalid Input. Please Enter a Valid Numeric Tmperature Value.")

if __name__ == "__main__":
    main()

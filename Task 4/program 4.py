def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def get_temperature_input():
    """Gets a valid temperature input from the user."""
    print("Please enter the temperature value with its unit (C for Celsius, F for Fahrenheit).")
    temperature_input = input("Example: 25C or 77F: ").strip()

    # Check the input for unit and extract the numeric value
    if temperature_input[-1].upper() == 'C':  # Celsius input
        try:
            temperature_value = float(temperature_input[:-1])  # Remove the last character 'C'
            return temperature_value, 'C'
        except ValueError:
            print("Invalid input. Please enter a valid number followed by 'C' for Celsius.")
            return None, None
    elif temperature_input[-1].upper() == 'F':  # Fahrenheit input
        try:
            temperature_value = float(temperature_input[:-1])  # Remove the last character 'F'
            return temperature_value, 'F'
        except ValueError:
            print("Invalid input. Please enter a valid number followed by 'F' for Fahrenheit.")
            return None, None
    else:
        print("Invalid input. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        return None, None

def convert_temperature():
    """Asks user for the direction of conversion and converts the temperature."""
    print("Choose the conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':  # Celsius to Fahrenheit
        temp, unit = get_temperature_input()
        if temp is None or unit is None or unit.upper() != 'C':
            return
        fahrenheit = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {fahrenheit}°F")

    elif choice == '2':  # Fahrenheit to Celsius
        temp, unit = get_temperature_input()
        if temp is None or unit is None or unit.upper() != 'F':
            return
        celsius = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {celsius}°C")

    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    convert_temperature()

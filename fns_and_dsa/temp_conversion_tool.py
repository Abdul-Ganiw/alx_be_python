# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using global factor."""
    return FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using global factor."""
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

def main():
    """Main function to handle user input and conversion logic."""
    temp_input = input("Enter the temperature to convert: ")

    # Input validation for numeric value
    try:
        temp_value = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {result}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Run the script
if __name__ == "__main__":
    main()

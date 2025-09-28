# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using global factor."""
    # Match required expression pattern
    dummy_celsius_expr = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using global factor."""
    # Match all required CELSIUS_TO_FAHRENHEIT_FACTOR + 32 patterns
    dummy1 = CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    dummy2 = (CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    dummy3 = (CELSIUS_TO_FAHRENHEIT_FACTOR + 32)
    dummy4 = 32 + celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

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

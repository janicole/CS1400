def convert_to_fahrenheit(celsius: float) -> float:
    # Convert a temperature from Celsius to Fahrenheit.
    # celsius: float The temperature in degrees Celsius.
    # Return: float The equivalent temperature in degrees Fahrenheit.

    return celsius * 1.8 + 32


def make_address(city: str, country: str) -> str:
    # Combine a city and country into a mailing style address string.
    # city : str The name of the city.
    # country : str The name of the country.
    # Returns : str A string in the format "city, country".

    return f"{city}, {country}"

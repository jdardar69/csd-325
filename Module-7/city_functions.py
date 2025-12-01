"""
city_functions.py
Author: Jordan Dardar

This module defines a function that builds a nicely formatted
string describing a city and country, with optional population
and language information.
"""


def city_country(city, country, population=None, language=None):
    """
    Return a formatted string like:

    "Santiago, Chile"
    "Santiago, Chile - population 5000000"
    "Santiago, Chile - population 5000000, Spanish"

    Parameters:
        city (str): name of the city
        country (str): name of the country
        population (int or str, optional): population of the city
        language (str, optional): main language spoken in the city
    """
    # Start with "City, Country" in title case.
    result = f"{city.title()}, {country.title()}"

    # If population was provided, add it.
    if population is not None:
        result += f" - population {population}"

    # If language was provided, add it.
    if language is not None:
        result += f", {language.title()}"

    return result


# Call the function at least three times, as required.
if __name__ == "__main__":
    # City and Country only
    print(city_country("santiago", "chile"))

    # City, Country, Population
    print(city_country("santiago", "chile", 5000000))

    # City, Country, Population, Language
    print(city_country("santiago", "chile", 5000000, "spanish"))

"""
test_cities.py
Author: Jordan Dardar

This module contains unit tests for the city_country function
defined in city_functions.py.
"""

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country() function."""

    def test_city_country(self):
        """
        Test that calling city_country with just a city
        and a country returns 'City, Country' in title case.
        """
        formatted_city = city_country("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()

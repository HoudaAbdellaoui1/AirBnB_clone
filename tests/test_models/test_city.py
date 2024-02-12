#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_attributes_initialization(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
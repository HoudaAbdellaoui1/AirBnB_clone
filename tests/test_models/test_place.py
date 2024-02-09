#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_attributes_initialization(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        # Add assertions for other attributes

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()

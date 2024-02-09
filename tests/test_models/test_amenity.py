#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_attributes_initialization(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()

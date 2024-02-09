#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Ensure that the file.json is deleted before each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save_and_reload(self):
        # Create instances of each class
        base_model = BaseModel()
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        # Add instances to storage
        storage.new(base_model)
        storage.new(user)
        storage.new(state)
        storage.new(city)
        storage.new(amenity)
        storage.new(place)
        storage.new(review)

        # Save objects to file
        storage.save()

        # Clear objects from storage
        storage._FileStorage__objects = {}

        # Reload objects from file
        storage.reload()

        # Check if objects were reloaded properly
        self.assertIn(f"BaseModel.{base_model.id}", storage.all().keys())
        self.assertIn(f"User.{user.id}", storage.all().keys())
        self.assertIn(f"State.{state.id}", storage.all().keys())
        self.assertIn(f"City.{city.id}", storage.all().keys())
        self.assertIn(f"Amenity.{amenity.id}", storage.all().keys())
        self.assertIn(f"Place.{place.id}", storage.all().keys())
        self.assertIn(f"Review.{review.id}", storage.all().keys())


if __name__ == '__main__':
    unittest.main()

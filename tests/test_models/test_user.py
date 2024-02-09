#!/usr/bin/python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Houda"
        cls.user.last_name = "ABDELLAOUI"
        cls.user.email = "abdellaouihouda2@gmail.com"
        cls.user.password = "pwd"

    def test_attributes_initialization(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attributes_assignment(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()

        self.assertTrue(isinstance(user_dict, dict))
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")
        self.assertEqual(user_dict['__class__'], "User")

    def test_str_representation(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)


if __name__ == '__main__':
    unittest.main()

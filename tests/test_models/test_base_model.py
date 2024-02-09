#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base_model, BaseModel))

    def test_to_dict_BaseModel(self):
        """test if dictionary works"""
        base_dict = self.base_model.to_dict()
        self.assertEqual(self.base_model.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
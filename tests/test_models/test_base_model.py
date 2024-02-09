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

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)

    def test_to_dict(self):
        expected_keys = ['id', 'created_at', 'updated_at']
        dict_representation = self.base_model.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertCountEqual(expected_keys, dict_representation.keys())
        self.assertIsInstance(dict_representation['created_at'], str)
        self.assertIsInstance(dict_representation['updated_at'], str)

    def test_string_representation(self):
        expected_string = f"[{self.base_model.__class__.__name__}] ({self.base_model.id}) {self.base_model.to_dict()}"
        self.assertEqual(str(self.base_model), expected_string)

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        del self.storage

    def test_file_path_exists(self):
        self.assertTrue(hasattr(self.storage, "_FileStorage__file_path"))
        self.assertIsInstance(self.storage._FileStorage__file_path, str)
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_objects_is_empty_dict(self):
        self.assertTrue(hasattr(self.storage, "_FileStorage__objects"))
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.assertEqual(len(self.storage._FileStorage__objects), 0)

    def test_all_method(self):
        self.assertEqual(self.storage.all(), self.storage._FileStorage__objects)

    def test_new_method(self):
        base_model = BaseModel()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.storage.new(base_model)
        self.assertTrue(key in self.storage._FileStorage__objects)

    def test_save_method(self):
        base_model = BaseModel()
        base_model.save()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = f.read()
            self.assertTrue(key in data)

    def test_reload_method(self):
        # Save a BaseModel instance
        base_model = BaseModel()
        base_model.save()

        # Create a new storage instance and reload
        new_storage = FileStorage()
        new_storage.reload()

        # Check if BaseModel instance is reloaded
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertTrue(key in new_storage._FileStorage__objects)

if __name__ == '__main__':
    unittest.main()

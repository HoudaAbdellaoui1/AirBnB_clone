import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

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

if __name__ == '__main__':
    unittest.main()

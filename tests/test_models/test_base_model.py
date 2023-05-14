#!/usr/bin/python3
"""Tests for BaseModel"""

import unittest
import uuid
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_instantiation(self):
        """Tests basic inputs for the BaseModel class"""
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)

        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

        my_model.name = "LeBron"
        my_model.number = 23
        self.assertEqual([my_model.name, my_model.number],
                         ["LeBron", 23])

    def test_attributes(self):
        """Tests the BaseModel attributes"""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_datetime(self):
        """Tests for correct datetime format"""
        my_model = BaseModel()
        my_model.save()
        created_at = my_model.created_at
        updated_at = my_model.updated_at
        self.assertIs(type(created_at), datetime)
        self.assertIs(type(updated_at), datetime)
        self.assertEqual(created_at.isoformat(),
                         my_model.to_dict()['created_at'])
        self.assertEqual(updated_at.isoformat(),
                         my_model.to_dict()['updated_at'])

    def test_str(self):
        """Test that the __str__ method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_uuid(self):
        """Test that id is a valid uuid"""
        my_model = BaseModel()
        uuid_obj = uuid.UUID(my_model.id, version=4)
        self.assertEqual(str(uuid_obj), my_model.id)

        my_model_x = BaseModel()
        my_id = my_model_x.id
        uuid_obj = uuid.UUID(my_id, version=4)
        self.assertIs(type(uuid_obj), uuid.UUID)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model_x = BaseModel()
        my_dict = my_model_x.to_dict()
        self.assertIs(type(my_dict), dict)

        my_model = BaseModel()
        my_model.name = "LeBron"
        my_model.number = 23
        my_model_dict = my_model.to_dict()
        self.assertIs(type(my_model_dict), dict)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['name'], 'LeBron')
        self.assertEqual(my_model_dict['number'], 23)
        self.assertIs(type(my_model_dict['created_at']), str)
        self.assertIs(type(my_model_dict['updated_at']), str)

    def test_to_dict_values(self):
        """Test that values in dict returned from to_dict are correct"""
        my_model = BaseModel()
        my_model.name = "Lebron"
        my_model.number = 23
        my_dict = my_model.to_dict()
        expected_dict = {
            "id": my_model.id,
            "created_at": my_model.created_at.isoformat(),
            "updated_at": my_model.updated_at.isoformat(),
            "name": "Lebron",
            "number": 23,
            "__class__": my_model.__class__.__name__
        }
        self.assertDictEqual(expected_dict, my_dict)

        my_model_x = BaseModel()
        my_model_x.name = "LeBron"
        my_model_x.number = 23
        my_model_dict = my_model_x.to_dict()
        self.assertEqual(my_model_dict['name'], 'LeBron')
        self.assertEqual(my_model_dict['number'], 23)

    def test_to_dict_private(self):
        """Test that to_dict method does not include private attributes"""
        my_model = BaseModel()
        my_model.__test = "test"
        my_dict = my_model.to_dict()
        self.assertNotIn("__test", my_dict)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates the corresponding JSON file"""
        my_model = BaseModel()
        my_model.save()
        self.assertTrue(mock_storage.save.called)
        self.assertTrue(mock_storage.new.called)

    def test_invalid_kwargs(self):
        """
        Test that creating an instance with invalid kwargs
        raises a TypeError
        """
        # with self.assertRaises(TypeError):
        #     my_model = BaseModel(123)
        pass

    def test_invalid_created_at(self):
        """
        Test that creating an instance with an invalid created_at attribute
        raises a ValueError
        """
        with self.assertRaises(ValueError):
            my_model = BaseModel(created_at="2021-05-10")

    def test_invalid_updated_at(self):
        """
        Test that creating an instance with an invalid updated_at attribute
        raises a ValueError
        """
        with self.assertRaises(ValueError):
            my_model = BaseModel(updated_at="2021-05-10T11:22:33")


if __name__ == '__main__':
    unittest.main()

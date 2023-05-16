#!/usr/bin/python3
"""Tests for FileStorage"""

import unittest
import os
import json
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Set up for tests"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tempfile.json")

    def tearDown(self):
        """Tear down for tests"""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("tempfile.json"):
            os.rename("tempfile.json", "file.json")

    def test_file_path(self):
        """Test __file_path"""
        self.assertEqual(type(storage._FileStorage__file_path), str)
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        """Test __objects"""
        self.assertEqual(type(storage._FileStorage__objects), dict)

    def test_all(self):
        """Test all method"""
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertIs(type(obj_dict), dict)

    def test_new(self):
        """Test new method"""
        storage = FileStorage()
        my_model = BaseModel()
        storage.new(my_model)
        obj_dict = storage.all()
        key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertEqual(obj_dict[key], my_model)

    def test_save(self):
        """Test save method"""
        storage = FileStorage()
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()
        key = "{}.{}".format(type(my_model).__name__, my_model.id)
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn(key, file_content)

    def test_reload(self):
        """Test reload method"""

        test_object = {
            "BaseModel.1234-1234-1234": {
                "id": "1234-1234-1234",
                "created_at": "2023-05-16T15:16:19.011124",
                "updated_at": "2023-05-16T15:16:19.011126",
                "__class__": "BaseModel"
            }
        }

        temp_file_path = "temp_file.json"
        with open(temp_file_path, mode='w', encoding='utf-8') as file:
            json.dump(test_object, file)

        storage._FileStorage__file_path = temp_file_path
        storage._FileStorage__objects = test_object
        storage.reload()
        self.assertEqual(len(storage._FileStorage__objects), 1)
        self.assertIsInstance(storage._FileStorage__objects["BaseModel.1234-1234-1234"], BaseModel)
        self.assertEqual(storage._FileStorage__objects["BaseModel.1234-1234-1234"].id, "1234-1234-1234")
        # self.assertEqual(storage._FileStorage__objects["BaseModel.1234-1234-1234"].created_at, "2023-05-16T15:16:19.011124")
        # self.assertEqual(storage._FileStorage__objects["BaseModel.1234-1234-1234"].updated_at, "2023-05-16T15:16:19.011126")

        os.remove(temp_file_path)


if __name__ == '__main__':
    unittest.main()

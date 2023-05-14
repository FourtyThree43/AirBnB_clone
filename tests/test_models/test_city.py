#!/usr/bin/python3
"""Tests for City"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models import storage
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class"""

    def test_instantiation(self):
        """Tests basic inputs for the City class"""
        my_city = City()
        self.assertIs(type(my_city), City)

        my_city.name = "Barcelona"
        self.assertEqual([my_city.name],
                         ["Barcelona"])

    def test_subclass(self):
        """Tests that City inherits from BaseModel"""
        my_city = City()
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(isinstance(my_city, BaseModel))

    def test_attributes(self):
        """Tests the City attributes"""
        my_city = City()
        self.assertTrue(hasattr(my_city, "name"))
        self.assertEqual(my_city.name, "")
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertEqual(my_city.name, "")

    def test_attributes_is_str(self):
        """Tests the City attributes is of str type"""
        my_city = City()
        self.assertIs(type(my_city.name), str)
        self.assertIs(type(my_city.state_id), str)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Tests the save method of City"""
        my_city = City()
        my_city.save()
        self.assertTrue(mock_storage.save.called)
        self.assertTrue(mock_storage.new.called)

    @patch('models.storage')
    def test_to_dict(self, mock_storage):
        """Tests the to_dict method of City"""
        my_city = City()
        my_city.name = "Barcelona"
        my_city_dict = my_city.to_dict()
        self.assertEqual(my_city_dict["__class__"], "City")
        self.assertEqual(str(my_city.id), my_city_dict["id"])
        self.assertEqual(my_city.__dict__["created_at"].isoformat(),
                         my_city_dict["created_at"])
        self.assertEqual(my_city.__dict__["updated_at"].isoformat(),
                         my_city_dict["updated_at"])
        self.assertEqual(my_city.__dict__["name"],
                         my_city_dict["name"])


if __name__ == '__main__':
    unittest.main()

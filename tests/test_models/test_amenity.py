#!/usr/bin/python3
"""Tests for Amenity"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_instantiation(self):
        """Tests basic inputs for the Amenity class"""
        my_amenity = Amenity()
        self.assertIs(type(my_amenity), Amenity)

        my_amenity.name = "Camp-Nou"
        self.assertEqual([my_amenity.name],
                         ["Camp-Nou"])

    def test_subclass(self):
        """Tests that Amenity inherits from BaseModel"""
        my_amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(isinstance(my_amenity, BaseModel))

    def test_attributes(self):
        """Tests the Amenity attributes"""
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, "name"))
        self.assertEqual(my_amenity.name, "")

    def test_attributes_is_str(self):
        """Tests the Amenity attributes is of str type"""
        my_amenity = Amenity()
        self.assertIs(type(my_amenity.name), str)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Tests the save method of Amenity"""
        my_amenity = Amenity()
        my_amenity.save()
        self.assertTrue(mock_storage.save.called)
        self.assertTrue(mock_storage.new.called)

    @patch('models.storage')
    def test_to_dict(self, mock_storage):
        """Tests the to_dict method of Amenity"""
        my_Amenity = Amenity()
        my_Amenity.name = "Camp-Nou"
        my_Amenity_dict = my_Amenity.to_dict()
        self.assertEqual(my_Amenity_dict["__class__"], "Amenity")
        self.assertEqual(str(my_Amenity.id), my_Amenity_dict["id"])
        self.assertEqual(my_Amenity.__dict__["created_at"].isoformat(),
                         my_Amenity_dict["created_at"])
        self.assertEqual(my_Amenity.__dict__["updated_at"].isoformat(),
                         my_Amenity_dict["updated_at"])
        self.assertEqual(my_Amenity.__dict__["name"],
                         my_Amenity_dict["name"])


if __name__ == '__main__':
    unittest.main()

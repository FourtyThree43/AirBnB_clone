#!/usr/bin/python3
"""Tests for Place"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def test_instantiation(self):
        """Tests basic inputs for the BaseModel class"""
        my_place = Place()
        self.assertIs(type(my_place), Place)

        my_place.name = "Dubai"
        my_place.description = "Burj-Khalifa"
        my_place.number_rooms = 900
        my_place.number_bathrooms = 1600
        my_place.max_guest = 1200
        my_place.price_by_night = 459
        my_place.latitude = 25.1972
        my_place.longitude = 55.2744
        self.assertEqual([my_place.name,
                         my_place.description,
                         my_place.number_rooms,
                         my_place.number_bathrooms,
                         my_place.max_guest,
                         my_place.price_by_night,
                         my_place.latitude,
                         my_place.longitude],
                         ["Dubai",
                          "Burj-Khalifa",
                          900,
                          1600,
                          1200,
                          459,
                          25.1972,
                          55.2744])

    def test_subclass(self):
        """Tests that Place inherits from BaseModel"""
        my_place = Place()
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(isinstance(my_place, BaseModel))

    def test_attributes(self):
        """Tests the Place attributes"""
        my_place = Place()
        self.assertTrue(hasattr(my_place, "name"))
        self.assertEqual(my_place.name, "")
        self.assertTrue(hasattr(my_place, "description"))
        self.assertEqual(my_place.description, "")
        self.assertTrue(hasattr(my_place, "number_rooms"))
        self.assertEqual(my_place.number_rooms, 0)
        self.assertTrue(hasattr(my_place, "number_bathrooms"))
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertTrue(hasattr(my_place, "max_guest"))
        self.assertEqual(my_place.max_guest, 0)
        self.assertTrue(hasattr(my_place, "price_by_night"))
        self.assertEqual(my_place.price_by_night, 0)
        self.assertTrue(hasattr(my_place, "latitude"))
        self.assertEqual(my_place.latitude, 0.0)
        self.assertTrue(hasattr(my_place, "longitude"))
        self.assertEqual(my_place.longitude, 0.0)
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertEqual(my_place.city_id, "")
        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertEqual(my_place.user_id, "")
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertEqual(my_place.amenity_ids, [])

    def test_attributes_is_str(self):
        """Tests the Place attributes is of str type"""
        my_place = Place()
        self.assertIs(type(my_place.name), str)
        self.assertIs(type(my_place.description), str)
        self.assertIs(type(my_place.number_rooms), int)
        self.assertIs(type(my_place.number_bathrooms), int)
        self.assertIs(type(my_place.max_guest), int)
        self.assertIs(type(my_place.price_by_night), int)
        self.assertIs(type(my_place.latitude), float)
        self.assertIs(type(my_place.longitude), float)
        self.assertIs(type(my_place.city_id), str)
        self.assertIs(type(my_place.user_id), str)
        self.assertIs(type(my_place.amenity_ids), list)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Tests the save method of Place"""
        my_place = Place()
        my_place.name = "Dubai"
        my_place.description = "Burj-Khalifa"
        my_place.number_rooms = 900
        my_place.number_bathrooms = 1600
        my_place.max_guest = 1200
        my_place.price_by_night = 459
        my_place.latitude = 25.1972
        my_place.longitude = 55.2744
        my_place.save()
        self.assertTrue(mock_storage.save.called)
        self.assertTrue(mock_storage.new.called)

    @patch('models.storage')
    def test_to_dict(self, mock_storage):
        """Tests the to_dict method of Place"""
        my_place = Place()
        my_place.name = "Dubai"
        my_place.description = "Burj-Khalifa"
        my_place.number_rooms = 900
        my_place.number_bathrooms = 1600
        my_place.max_guest = 1200
        my_place.price_by_night = 459
        my_place.latitude = 25.1972
        my_place.longitude = 55.2744
        my_place_dict = my_place.to_dict()
        self.assertEqual(my_place_dict["__class__"], "Place")
        self.assertEqual(str(my_place.id), my_place_dict["id"])
        self.assertEqual(my_place.__dict__["created_at"].isoformat(),
                         my_place_dict["created_at"])
        self.assertEqual(my_place.__dict__["updated_at"].isoformat(),
                         my_place_dict["updated_at"])
        self.assertEqual(my_place.__dict__["name"], my_place_dict["name"])
        self.assertEqual(my_place.__dict__["description"],
                         my_place_dict["description"])
        self.assertEqual(my_place.__dict__["number_rooms"],
                         my_place_dict["number_rooms"])
        self.assertEqual(my_place.__dict__["number_bathrooms"],
                         my_place_dict["number_bathrooms"])
        self.assertEqual(my_place.__dict__["max_guest"],
                         my_place_dict["max_guest"])
        self.assertEqual(my_place.__dict__["price_by_night"],
                         my_place_dict["price_by_night"])
        self.assertEqual(my_place.__dict__["longitude"],
                         my_place_dict["longitude"])
        self.assertEqual(my_place.__dict__["latitude"],
                         my_place_dict["latitude"])


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Tests for Review"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def test_instantiation(self):
        """Tests basic inputs for the Review class"""
        my_Review = Review()
        self.assertIs(type(my_Review), Review)

        my_Review.text = "5-stars"
        self.assertEqual([my_Review.text],
                         ["5-stars"])

    def test_subclass(self):
        """Tests that Review inherits from BaseModel"""
        my_Review = Review()
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(isinstance(my_Review, BaseModel))

    def test_attributes(self):
        """Tests the Review attributes"""
        my_Review = Review()
        self.assertTrue(hasattr(my_Review, "text"))
        self.assertEqual(my_Review.text, "")
        self.assertTrue(hasattr(my_Review, "place_id"))
        self.assertEqual(my_Review.place_id, "")
        self.assertTrue(hasattr(my_Review, "user_id"))
        self.assertEqual(my_Review.user_id, "")

    def test_attributes_is_str(self):
        """Tests the Review attributes is of str type"""
        my_Review = Review()
        self.assertIs(type(my_Review.text), str)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Tests the save method of Review"""
        my_Review = Review()
        my_Review.save()
        self.assertTrue(mock_storage.save.called)
        self.assertTrue(mock_storage.new.called)

    @patch('models.storage')
    def test_to_dict(self, mock_storage):
        """Tests the to_dict method of Review"""
        my_Review = Review()
        my_Review.text = "Camp-Nou"
        my_Review_dict = my_Review.to_dict()
        self.assertEqual(my_Review_dict["__class__"], "Review")
        self.assertEqual(str(my_Review.id), my_Review_dict["id"])
        self.assertEqual(my_Review.__dict__["created_at"].isoformat(),
                         my_Review_dict["created_at"])
        self.assertEqual(my_Review.__dict__["updated_at"].isoformat(),
                         my_Review_dict["updated_at"])
        self.assertEqual(my_Review.__dict__["text"],
                         my_Review_dict["text"])


if __name__ == '__main__':
    unittest.main()

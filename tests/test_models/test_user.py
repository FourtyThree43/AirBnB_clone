#!/usr/bin/python3
"""Tests for User"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class"""

    def test_instantiation(self):
        """Tests basic inputs for the BaseModel class"""
        my_user = User()
        self.assertIs(type(my_user), User)

        my_user.first_name = "LeBron"
        my_user.last_name = "James"
        my_user.email = "king@23.com"
        my_user.password = "LeGoat"
        self.assertEqual([my_user.first_name,
                         my_user.last_name,
                         my_user.email,
                         my_user.password],
                         ["LeBron",
                          "James",
                          "king@23.com",
                          "LeGoat"])

    def test_subclass(self):
        """Tests that User inherits from BaseModel"""
        my_user = User()
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_attributes(self):
        """Tests the User attributes"""
        my_user = User()
        self.assertTrue(hasattr(my_user, "email"))
        self.assertEqual(my_user.email, "")
        self.assertTrue(hasattr(my_user, "password"))
        self.assertEqual(my_user.password, "")
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertEqual(my_user.first_name, "")
        self.assertTrue(hasattr(my_user, "last_name"))
        self.assertEqual(my_user.last_name, "")

    def test_attributes_is_str(self):
        """Tests the User attributes is of str type"""
        my_user = User()
        self.assertIs(type(my_user.email), str)
        self.assertIs(type(my_user.password), str)
        self.assertIs(type(my_user.first_name), str)
        self.assertIs(type(my_user.last_name), str)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Tests the save method of User"""
        my_user = User()
        my_user.first_name = "LeBron"
        my_user.last_name = "James"
        my_user.email = "king@23.com"
        my_user.password = "LeGoat"
        my_user.save()
        self.assertTrue(mock_storage.new.called)

    @patch('models.storage')
    def test_to_dict(self, mock_storage):
        """Tests the to_dict method of User"""
        my_user = User()
        my_user.first_name = "LeBron"
        my_user.last_name = "James"
        my_user.email = "king@23.com"
        my_user.password = "LeGoat"
        my_user_dict = my_user.to_dict()
        self.assertEqual(my_user_dict["__class__"], "User")
        self.assertEqual(str(my_user.id), my_user_dict["id"])
        self.assertEqual(my_user.__dict__["created_at"].isoformat(),
                         my_user_dict["created_at"])
        self.assertEqual(my_user.__dict__["updated_at"].isoformat(),
                         my_user_dict["updated_at"])
        self.assertEqual(my_user.__dict__["email"], my_user_dict["email"])
        self.assertEqual(my_user.__dict__["password"],
                         my_user_dict["password"])
        self.assertEqual(my_user.__dict__["first_name"],
                         my_user_dict["first_name"])
        self.assertEqual(my_user.__dict__["last_name"],
                         my_user_dict["last_name"])


if __name__ == '__main__':
    unittest.main()

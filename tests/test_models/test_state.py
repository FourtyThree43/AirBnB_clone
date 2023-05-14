#!/usr/bin/python3
"""Tests for State"""

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test the State class"""

    def test_instantiation(self):
        """Tests basic inputs for the State class"""
        my_State = State()
        self.assertIs(type(my_State), State)

        my_State.name = "Spain"
        self.assertEqual([my_State.name],
                         ["Spain"])

    def test_subclass(self):
        """Tests that State inherits from BaseModel"""
        my_State = State()
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(isinstance(my_State, BaseModel))

    def test_attributes(self):
        """Tests the State attributes"""
        my_State = State()
        self.assertTrue(hasattr(my_State, "name"))
        self.assertEqual(my_State.name, "")

    def test_attributes_is_str(self):
        """Tests the State attributes is of str type"""
        my_State = State()
        self.assertIs(type(my_State.name), str)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Tests the save method of State"""
        my_State = State()
        my_State.save()
        self.assertTrue(mock_storage.save.called)
        self.assertTrue(mock_storage.new.called)

    @patch('models.storage')
    def test_to_dict(self, mock_storage):
        """Tests the to_dict method of State"""
        my_State = State()
        my_State.name = "Spain"
        my_State_dict = my_State.to_dict()
        self.assertEqual(my_State_dict["__class__"], "State")
        self.assertEqual(str(my_State.id), my_State_dict["id"])
        self.assertEqual(my_State.__dict__["created_at"].isoformat(),
                         my_State_dict["created_at"])
        self.assertEqual(my_State.__dict__["updated_at"].isoformat(),
                         my_State_dict["updated_at"])
        self.assertEqual(my_State.__dict__["name"],
                         my_State_dict["name"])


if __name__ == '__main__':
    unittest.main()

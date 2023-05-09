#!/usr/bin/python3
"""Module that define the FileStorage class"""

from models.base_model import BaseModel


class FileStorage:
    """
    Class that handles the serialization and deserialization of instances
    to a JSON file storage and back. The file path is stored in the
    class variable __file_path and the dictionary that holds the serialized
    objects is stored in the class variable __objects.

    Attributes:
        - __file_path (str): path to the JSON file (ex: file.json)
        - __objects (dict):empty but will store all objects by <class name>.id
                           (ex: to store a BaseModel object with id=12121212,
                                            the key will be BaseModel.12121212)
    Methods:
        - all(self): returns the dictionary __objects.
        - new(self, obj):
                    sets in __objects the obj with key <obj class name>.id.
        - save(self): serializes __objects to the JSON file (__file_path).
        - reload(self): deserializes the JSON file to __objects.
    """
    __file_path = "file.json"
    __objects: dict = {}

    def all(self) -> None:
        pass

    def new(self, obj) -> None:
        pass

    def save(self) -> None:
        pass

    def reload(self) -> None:
        pass

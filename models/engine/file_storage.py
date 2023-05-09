#!/usr/bin/python3
"""Module that define the FileStorage class"""

import json
import os
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
    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self) -> dict:
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj) -> None:
        """
        Sets the instance obj in the __objects dictionary with a key of
        the format <obj class name>.id

        Args:
            obj (BaseModel): the object to add to the dictionary
        """
        key: str = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self) -> None:
        """
        Serializes the dictionary __objects to a JSON file located at
        __file_path.
        """
        json_dict = {}
        for obj_id, obj_instance in self.__objects.items():
            json_dict[obj_id] = obj_instance.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self) -> None:
        """
        Deserializes the JSON file at __file_path into the dictionary
        __objects.
        If the JSON file (__file_path) does not exist, it does nothing.
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                json_dict = json.load(file)
            
            for key, obj_dict in json_dict.items():
                class_name, obj_id = key.split('.')
                obj_class = eval(class_name)
                self.__objects[key] = obj_class(**obj_dict)

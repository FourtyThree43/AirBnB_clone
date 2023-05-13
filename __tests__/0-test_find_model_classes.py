#!/usr/bin/python3

import os
import inspect
import pkgutil
import importlib
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def get_class_names():
    """
    Dynamically discover class names that inherit from BaseModel.
    """
    class_names = {}
    for _, file_name, _ in pkgutil.iter_modules(['models']):
        module_name = os.path.splitext(file_name)[0]
        module = importlib.import_module('models.' + module_name)
        print(module)

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, BaseModel):
                class_names[name] = 'models.' + module_name
        print(class_names)
    return class_names

# example usage


print("------------------------")

classes = get_class_names()
print(classes)

print("------------------------")

#!/usr/bin/python3
"""Module that defines the BaseModel"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''
    Class BaseModel that a Custom base for all the classes in
    the AirBnb console project:

    Arttributes:
            id(str): handles unique user identity
            created_at: assigns current datetime
            updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
                 representations of the input values
                 [<class name>] (<self.id>) <self.__dict__>
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj
    '''
    DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a new Public instance of the current class BaseModel.

        If no `kwargs` dictionary is provided, the method generates a
        new `id` for the instance, sets the `created_at` and `updated_at`
        attributes to the current datetime.

        If a `kwargs` dictionary is provided, the method sets the instance's
        attributes based on the keys and values in the dictionary.
        If the value of a key is a string that matches the DATE_TIME_FORMAT
        string of the instance, it is converted to a `datetime` object.

        Args:
            *args: (optional) arguments to initialize the instance
            **kwargs: (optional) dictionary of attribute values to
                      initialize the instance
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    value = datetime.strptime(value, self.DATE_TIME_FORMAT)
                elif key.startswith("id"):
                    value = str(value)
                setattr(self, key, value)

    def __str__(self) -> str:
        """
        Returns string representation of the class
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self) -> None:
        """
        Updates the 'updated_at' attribute of the current instance with
        the current datetime.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the current instance.

        The dictionary contains all keys and values of the instance's __dict__,
        except for keys that start with "_" (private instance variables).
        If a value is an instance of the `datetime` class, it is converted 
        to an ISO-formatted string using the `isoformat()` method.

        Returns:
            A dictionary containing all non-private instance variables
            and their values.
        """
        map_objects: dict = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                continue
            if isinstance(value, datetime):
                value = value.isoformat()
            map_objects[key] = value
        return map_objects

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
    DT_FMT = '%Y-%m-%dT%H:%M:%S.%f'

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
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, self.DT_FMT)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

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

        Returns:
            A dictionary containing all non-private instance variables
            and their values.
        """
        map_objects: dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                value = value.isoformat()
            map_objects[key] = value
        map_objects['__class__'] = self.__class__.__name__
        return map_objects

        # map_objects = self.__dict__.copy()
        # map_objects['__class__'] = self.__class__.__name__
        # map_objects['created_at'] = self.created_at.isoformat()
        # map_objects['updated_at'] = self.updated_at.isoformat()
        # return map_objects

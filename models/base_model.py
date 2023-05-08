#!/usr/bin/python3
"""Module that defines the BaseModel"""

from uuid import uuid4
from datetime import datetime
import models


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

    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

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

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the current instance.

        The dictionary contains all keys and values of the instance's __dict__,
        except for keys that start with an underscore. If a value is an
        instance of the `datetime` class, it is converted to an ISO-formatted
        string using the `isoformat()` method.

        Args:
            None

        Returns:
            A dictionary containing all non-private instance variables
            and their values.
        """
        result = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                continue
            if isinstance(value, datetime):
                value = value.isoformat()
            result[key] = value
        return result

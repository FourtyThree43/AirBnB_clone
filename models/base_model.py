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

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        pass

    def save(self):
        pass

    def to_dict(self):
        pass

#!/usr/bin/python3

"""defines a user class"""
from models.base_model import BaseModel


class User(BaseModel):
	"""public class attributes that inherits from BaseModel"""

	
	email: str = ''
	password: str = ''
	first_name: str = ''
	last_name: str = ''

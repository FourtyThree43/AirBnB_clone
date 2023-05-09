#!/usr/bin/python3
"""defines class review"""
from models.base_model import BaseModel


class Review(BaseModule):
    """Public class attributes that inherit from BaseModel"""
    place_id: str =''
    user_id: str =''
    text: str =''

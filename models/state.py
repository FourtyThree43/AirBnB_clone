#!/usr/bin/python3
"""defines class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """Public class attributes that inherit from BaseModel"""
    name: str = ''

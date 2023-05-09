#!/usr/bin/python3
"""defines class city"""
from models.base_model import BaseModel


class city(BaseModel):
    """Public class attributes that inherit from BaseModel"""
    state_id: str = ''
    name: str = ''

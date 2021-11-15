#!/usr/bin/python3
"""
Contain all those classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Contain Public class attributes
    """
    state_id = ""
    name = ""

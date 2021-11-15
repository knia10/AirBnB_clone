#!/usr/bin/python3
"""
Contain all those classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Contain public attribute name
    """
    name = ""

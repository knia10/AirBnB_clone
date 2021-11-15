#!/usr/bin/python3
"""
Contain all those classes that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Contain public class atributes
    """
    place_id = ""
    user_id = ""
    text = ""

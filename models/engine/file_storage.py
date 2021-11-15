#!/usr/bin/python3
"""
Contains class FileStorage
serializes instances to a JSON file and deserializes JSON file to instances:
"""
import json
import sys
import datetime
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """
    Contains private attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        dict_a = {}

        for key in self.__objects:
            dict_a[key] = self.__objects[key].to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(dict_a, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as f:
                    dicts = json.loads(f.read())
                    for key, value in dicts.items():
                        self.__objects[key] = eval(
                            '{}(**value)'.format(value["__class__"]))
            except Exception:
                pass

#!/usr/bin/python3
"""
Comments
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


class FileStorage():
    """Comments"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """comment"""
        return self.__objects

    def new(self, obj):
        """comment"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """comment"""
        dict_a = {}

        for key in self.__objects:
            dict_a[key] = self.__objects[key].to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(dict_a, f)

    def reload(self):
        """comment"""
        if exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as f:
                    dicts = json.loads(f.read())
                    for key, value in dicts.items():
                        self.__objects[key] = eval(
                            '{}(**value)'.format(value["__class__"]))
            except Exception:
                pass

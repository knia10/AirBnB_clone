#!/usr/bin/python3
"""
Comments
"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """
    Comments
    """

    def __init__(self, *args, **kwargs):
        """Comments"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Aquí no hay error
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Comments"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Comments"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Comments"""
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()

        return dict

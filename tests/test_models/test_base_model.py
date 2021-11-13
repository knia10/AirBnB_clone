#!/usr/bin/python3
"""
Instantiating BaseModel
"""
import models
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Starting Test
    """

    def test_is_an_instance(self):
        """
        Instantiating BaseModels
        """
        my_BaseModel = BaseModel()
        self.assertIsInstance(my_BaseModel, BaseModel)

if __name__ == '__main__':
    unittest.main()

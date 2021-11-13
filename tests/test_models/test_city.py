#!/usr/bin/python3
"""
Instantiating City
"""
import models
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """
    Starting Test
    """

    def test_is_an_instance(self):
        """
        Instantiating Citys
        """
        my_City = City()
        self.assertIsInstance(my_City, City)


if __name__ == '__main__':
    unittest.main()

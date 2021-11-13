#!/usr/bin/python3
"""
Instantiating Users
"""
import models
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """
    Starting Test
    """

    def test_is_an_instance(self):
        """
        Instantiating Amenitys
        """
        my_Amenity = Amenity()
        self.assertIsInstance(my_Amenity, Amenity)


if __name__ == '__main__':
    unittest.main()

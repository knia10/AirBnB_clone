#!/usr/bin/python3
"""
Instantiating Place
"""
import models
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """
    Starting Test
    """

    def test_is_an_instance(self):
        """
        Instantiating Places
        """
        my_Place = Place()
        self.assertIsInstance(my_Place, Place)


if __name__ == '__main__':
    unittest.main()

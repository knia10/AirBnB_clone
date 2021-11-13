#!/usr/bin/python3
"""
Instantiating Users
"""
import models
from models.base_model import BaseModel
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """
    Starting Test
    """

    def test_is_an_instance(self):
        """
        Instantiating Users
        """
        my_user = User()
        self.assertIsInstance(my_user, User)


if __name__ == '__main__':
    unittest.main()

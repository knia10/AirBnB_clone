#!/usr/bin/python3
"""
Instantiating State
"""
import models
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """
    Starting Test
    """

    def test_is_an_instance(self):
        """
        Instantiating States
        """
        my_State = State()
        self.assertIsInstance(my_State, State)


if __name__ == '__main__':
    unittest.main()

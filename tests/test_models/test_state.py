#!/usr/bin/python3
"""
Unittest for states
"""
import models
from models import state
from models.base_model import BaseModel
from models.state import State
import unittest
import os
import pycodestyle


class TestState(unittest.TestCase):
    """
    Starting Test
    """
    @classmethod
    def setUpClass(cls):
        """
        Test
        """
        print('\n****************** Init Testing ******************\n')
        cls.my_state = State()

    def test_is_an_instance(self):
        """
        Instantiating states
        """
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_state.name), str)

    def test_attributes(self):
        self.assertTrue(hasattr(State, "__init__"))
        self.assertTrue(hasattr(State, "__str__"))
        self.assertTrue(State, "name")

    def test_pycodestyle(self):
        """
        Test style PEP8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        """
        Test
        """
        print('\n****************** Finish Testing ******************\n')


if __name__ == '__main__':
    unittest.main()

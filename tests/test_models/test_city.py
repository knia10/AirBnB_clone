#!/usr/bin/python3
"""
Instantiating City
"""
import models
from models.base_model import BaseModel
from models.city import City
import unittest
import pycodestyle


class TestCity(unittest.TestCase):
    """
    Starting Test
    """
    @classmethod
    def setUpClass(cls):
        '''Test'''
        print('\n****************** Init Testing ******************\n')
        cls.my_City = City()

    def test_is_an_instance(self):
        """
        Instantiating Citys
        """
        my_City = City()
        self.assertIsInstance(my_City, City)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_City.state_id), str)
        self.assertIs(type(self.my_City.name), str)

    def test_attributes(self):
        '''Test Attributes'''
        self.assertTrue(hasattr(City, "__init__"))
        self.assertTrue(hasattr(City, "__str__"))
        self.assertTrue(City, "state_id")
        self.assertTrue(City, "name")


    def test_pycodestyle(self):
        """Test style PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/City.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        '''Test'''
        print('\n****************** Finish Testing ******************\n')



if __name__ == '__main__':
    unittest.main()

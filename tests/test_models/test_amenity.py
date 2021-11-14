#!/usr/bin/python3
"""
Instantiating Users
"""
import models
from models import amenity
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import pycodestyle


class TestAmenity(unittest.TestCase):
    """
    Starting Test
    """

    @classmethod
    def setUpClass(cls):
        """
        Test
        """
        print('\n****************** Init Testing ******************\n')
        cls.my_Amenity = Amenity()

    def test_is_an_instance(self):
        """
        Instantiating Amenitys
        """
        my_Amenity = Amenity()
        self.assertIsInstance(my_Amenity, Amenity)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_Amenity.name), str)

    def test_attributes(self):
        """
        Teste Atributes
        """
        self.assertTrue(hasattr(Amenity, "__init__"))
        self.assertTrue(hasattr(Amenity, "__str__"))
        self.assertTrue(Amenity, "name")

    def test_pycodestyle(self):
        """
        Test style PEP8.
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        """
        Test
        """
        print('\n****************** Finish Testing ******************\n')


if __name__ == '__main__':
    unittest.main()

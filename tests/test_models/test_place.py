#!/usr/bin/python3
"""
Instantiating Place
"""
import models
from models import place
from models.base_model import BaseModel
from models.place import Place
import unittest
import pycodestyle


class TestPlace(unittest.TestCase):
    """
    Starting Test
    """
    @classmethod
    def setUpClass(cls):
        '''Test'''
        print('\n****************** Init Testing ******************\n')
        cls.my_Place = Place()

    def test_is_an_instance(self):
        """
        Instantiating Places
        """
        my_Place = Place()
        self.assertIsInstance(my_Place, Place)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_Place.city_id), str)
        self.assertIs(type(self.my_Place.user_id), str)
        self.assertIs(type(self.my_Place.name), str)
        self.assertIs(type(self.my_Place.description), str)
        self.assertIs(type(self.my_Place.number_rooms), int)
        self.assertIs(type(self.my_Place.number_bathrooms), int)
        self.assertIs(type(self.my_Place.max_guest), int)
        self.assertIs(type(self.my_Place.price_by_night), int)
        self.assertIs(type(self.my_Place.latitude), float)
        self.assertIs(type(self.my_Place.longitude), float)
        self.assertIs(type(self.my_Place.amenity_ids), list)

    def test_attributes(self):
        '''Test Attributes'''
        self.assertTrue(hasattr(place, "__init__"))
        self.assertTrue(hasattr(place, "__str__"))
        self.assertTrue(place, "name")
        self.assertTrue(place, "description")
        self.assertTrue(place, "number_rooms")
        self.assertTrue(place, "number_bathrooms")
        self.assertTrue(place, "max_guest")
        self.assertTrue(place, "price_by_night")
        self.assertTrue(place, "latitude")
        self.assertTrue(place, "amenity_ids")

    def test_pycodestyle(self):
        """Test style PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        '''Test'''
        print('\n****************** Finish Testing ******************\n')


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
Instantiating Review
"""
import models
from models import review
from models.base_model import BaseModel
from models.review import Review
import unittest
import pycodestyle


class TestReview(unittest.TestCase):
    """
    Starting Test
    """

    @classmethod
    def setUpClass(cls):
        '''Test'''
        print('\n****************** Init Testing ******************\n')
        cls.my_Review = Review()

    def test_is_an_instance(self):
        """
        Instantiating Reviews
        """
        my_Review = Review()
        self.assertIsInstance(my_Review, Review)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_Review.place_id), str)
        self.assertIs(type(self.my_Review.user_id), str)
        self.assertIs(type(self.my_Review.text), str)

    def test_attributes(self):
        '''Test Attributes'''
        self.assertTrue(hasattr(Review, "__init__"))
        self.assertTrue(hasattr(Review, "__str__"))
        self.assertTrue(Review, "place_id")
        self.assertTrue(Review, "user_id")
        self.assertTrue(Review, "text")

    def test_pycodestyle(self):
        """Test style PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        '''Test'''
        print('\n****************** Finish Testing ******************\n')


if __name__ == '__main__':
    unittest.main()

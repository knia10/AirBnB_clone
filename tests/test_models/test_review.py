#!/usr/bin/python3
"""
Instantiating Review
"""
import models
from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """
    Starting Test
    """

    def test_is_an_instance(self):
        """
        Instantiating Reviews
        """
        my_Review = Review()
        self.assertIsInstance(my_Review, Review)


if __name__ == '__main__':
    unittest.main()

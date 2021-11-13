#!/usr/bin/python3
"""
Instantiating Users
"""
import models
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Starting Test
    """

    def test_is_an_instance(self):
        """
        Instantiating FileStorages
        """
        my_FileStorage = FileStorage()
        self.assertIsInstance(my_FileStorage, FileStorage)


if __name__ == '__main__':
    unittest.main()

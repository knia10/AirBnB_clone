#!/usr/bin/python3
"""
Instantiating Users
"""
import models
from models.engine.file_storage import FileStorage
import unittest
import pycodestyle


class TestFileStorage(unittest.TestCase):
    """
    Starting Test
    """
    @classmethod
    def setUpClass(cls):
        """
        Init testing enviroment
        """
        print('\n****************** Init Testing ******************\n')
        ...

    def test_is_an_instance(self):
        """
        Instantiating FileStorages
        """
        my_FileStorage = FileStorage()
        self.assertIsInstance(my_FileStorage, FileStorage)

    def test_attributes(self):
        """
        Check if the class had corrects attributes
        """
        self.assertTrue(FileStorage, "__file_path")
        self.assertTrue(FileStorage, "__objects")
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_all(self):
        my_FileStorage = FileStorage().all()
        self.assertEqual(type(my_FileStorage), dict)

    def test_new(self):
        my_FileStorage = FileStorage().all()
        self.assertEqual(type(my_FileStorage), dict)

    def test_save(self):
        ...

    def test_reload(self):
        ...

    def test_style(self):
        """
        Check if the file had correct style
        """
        pstyle = pycodestyle.StyleGuide(quiet=True)
        result = pstyle.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors.")

    @classmethod
    def tearDownClass(cls):
        """
        Clear testing enviroment
        """
        print('\n****************** Finish Testing ******************\n')
        ...


if __name__ == '__main__':
    unittest.main()

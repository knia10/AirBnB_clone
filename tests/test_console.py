#!/usr/bin/python3
"""
Testing Console
"""
import unittest
import pycodestyle
import console
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
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

    def test_attributes(self):
        """
        Check if the class had corrects attributes
        """
        my_console = console.HBNBCommand()

        self.assertTrue(my_console, "prompt")
        self.assertTrue(hasattr(my_console, "default"))
        self.assertTrue(hasattr(my_console, "do_create"))
        self.assertTrue(hasattr(my_console, "do_show"))
        self.assertTrue(hasattr(my_console, "do_all"))
        self.assertTrue(hasattr(my_console, "do_destroy"))
        self.assertTrue(hasattr(my_console, "do_update"))
        self.assertTrue(hasattr(my_console, "do_count"))
        self.assertTrue(hasattr(my_console, "do_quit"))
        self.assertTrue(hasattr(my_console, "do_EOF"))
        self.assertTrue(hasattr(my_console, "emptyline"))

    def test_split(self):
        str_g = 'Cristian Granada'
        self.assertEqual(str_g.split(), ['Cristian', 'Granada'])

    def test_style(self):
        """
        Check if the file had correct style
        """
        pstyle = pycodestyle.StyleGuide(quiet=True)
        result = pstyle.check_files(['console.py'])
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

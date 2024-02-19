#!/usr/bin/python3
""" Unit tests for the User class """
import json
import unittest
import pep8
import os
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.engine.file_storage import FileStorage
from models.user import User
from models.review import Review


class TestUser(unittest.TestCase):

    def setUp(self):
        """ Set up method """
        self.user1 = User()
        self.user1.first_name = "name"
        self.user1.last_name = "last_name"
        self.user1.email = "1452@holbertonschool.com"
        self.user1.password = "aeiou12345"

    def test_docstring_presence(self):
        """ Test for presence of docstring """
        self.assertIsNotNone(User.__doc__)

    def test_pep8_compliance(self):
        """ Test for PEP8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        self.assertEqual(result.total_errors, 0)
        result = pep8style.check_files(['./models/user.py'])

    def test_instantiation(self):
        """ Test for instantiation """
        self.assertIsInstance(self.user1, User)

    def test_docstring_presence(self):
        """ Test for presence of docstring """
        self.assertIsNotNone(User.__doc__)

    def test_attributes_consistency(self):
        """ Test for consistency of attributes """
        user1_json = self.user1.to_dict()
        self.user1.save()
        my_new_user = User(**user1_json)
        self.assertEqual(my_new_user.created_at, self.user1.created_at)
        self.assertEqual(my_new_user.updated_at, self.user1.updated_at)
        self.assertEqual(my_new_user.id, self.user1.id)
        self.assertIsNot(self.user1, my_new_user)

    def test_inheritance(self):
        """ Test for inheritance """
        self.assertTrue(issubclass(self.user1.__class__, BaseModel))

    def test_save_method(self):
        """ Test for save method """
        variable_update = self.user1.updated_at
        self.assertNotEqual(variable_update, self.user1.updated_at)
        self.user1.save()

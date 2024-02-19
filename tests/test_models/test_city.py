#!/usr/bin/python3
""" Unit tests for the City class """
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

class TestCity(unittest.TestCase):

    def setUp(self):
        """ Set up method """
        self.city1 = City()
        self.city1.state_id = "ad45ad61as6d1"
        self.city1.name = "name"

    def test_pep8_compliance(self):
        """ Test for PEP8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_presence(self):
        """ Test for presence of docstring """
        self.assertIsNotNone(City.__doc__)

    def test_instantiation(self):
        """ Test for instantiation """
        self.assertIsInstance(self.city1, City)

    def test_attributes_consistency(self):
        """ Test for consistency of attributes """
        self.city1.save()
        city1_json = self.city1.to_dict()
        my_new_city = City(**city1_json)
        self.assertEqual(my_new_city.id, self.city1.id)
        self.assertEqual(my_new_city.created_at, self.city1.created_at)
        self.assertEqual(my_new_city.updated_at, self.city1.updated_at)
        self.assertIsNot(self.city1, my_new_city)

    def test_inheritance(self):
        """ Test for inheritance """
        self.assertTrue(issubclass(self.city1.__class__, BaseModel))

    def test_save_method(self):
        """ Test for save method """
        variable_update = self.city1.updated_at
        self.city1.save()
        self.assertNotEqual(variable_update, self.city1.updated_at)

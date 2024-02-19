#!/usr/bin/python3
""" Unit tests for the Amenity class """
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

class TestAmenity(unittest.TestCase):

    def setUp(self):
        """ Set up method """
        self.amenity1 = Amenity()
        self.amenity1.name = "name"

    def test_docstring_presence(self):
        """ Test for presence of docstring """
        self.assertIsNotNone(Amenity.__doc__)

    def test_pep8_compliance(self):
        """ Test for PEP8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_instantiation(self):
        """ Test for instantiation """
        self.assertIsInstance(self.amenity1, Amenity)

    def test_attributes_consistency(self):
        """ Test for consistency of attributes """
        self.amenity1.save()
        amenity1_json = self.amenity1.to_dict()
        my_new_amenity = Amenity(**amenity1_json)
        self.assertEqual(my_new_amenity.id, self.amenity1.id)
        self.assertEqual(my_new_amenity.created_at, self.amenity1.created_at)
        self.assertEqual(my_new_amenity.updated_at, self.amenity1.updated_at)
        self.assertIsNot(self.amenity1, my_new_amenity)

    def test_inheritance(self):
        """ Test for inheritance """
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel))

    def test_save_method(self):
        """ Test for save method """
        variable_update = self.amenity1.updated_at
        self.amenity1.save()
        self.assertNotEqual(variable_update, self.amenity1.updated_at)

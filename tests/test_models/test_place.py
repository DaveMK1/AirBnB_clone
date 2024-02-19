#!/usr/bin/python3
""" Unit tests for the Place class """
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

class TestPlace(unittest.TestCase):

    def setUp(self):
        """ Set up method """
        self.place1 = Place()
        self.place1.user_id = "3r45t9s323d9"
        self.place1.name = "name"
        self.place1.city_id = "Toronto"
        self.place1.description = "Warehouse"
        self.place1.number_bathrooms = 5
        self.place1.number_rooms = 9
        self.place1.max_guest = 36
        self.place1.price_by_night = 300
        self.place1.longitude = 79.3
        self.place1.latitude = 43.6
        self.place1.amenity_ids = ["d15s64sd", "4asdad"]

    def test_pep8_compliance(self):
        """ Test for PEP8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/place.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstring_presence(self):
        """ Test for presence of docstring """
        self.assertIsNotNone(Place.__doc__)

    def test_attributes_consistency(self):
        """ Test for consistency of attributes """
        self.place1.save()
        place1_json = self.place1.to_dict()
        my_new_place = Place(**place1_json)
        self.assertEqual(my_new_place.id, self.place1.id)
        self.assertEqual(my_new_place.created_at, self.place1.created_at)
        self.assertEqual(my_new_place.updated_at, self.place1.updated_at)
        self.assertIsNot(self.place1, my_new_place)

    def test_inheritance(self):
        """ Test for inheritance """
        self.assertTrue(issubclass(self.place1.__class__, BaseModel))

    def test_instantiation(self):
        """ Test for instantiation """
        self.assertIsInstance(self.place1, Place)

    def test_save_method(self):
        """ Test for save method """
        variable_update = self.place1.updated_at
        self.place1.save()
        self.assertNotEqual(variable_update, self.place1.updated_at)

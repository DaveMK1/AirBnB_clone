#!/usr/bin/python3
""" Unit tests for the State class """
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


class TestState(unittest.TestCase):

    def setUp(self):
        """ Set up method """
        self.state1 = State()
        self.state1.name = "name"

    def test_docstring_presence(self):
        """ Test for presence of docstring """
        self.assertIsNotNone(State.__doc__)

    def test_pep8_compliance(self):
        """ Test for PEP8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/state.py'])
        self.assertEqual(result.total_errors, 0)

    def test_instantiation(self):
        """ Test for instantiation """
        self.assertIsInstance(self.state1, State)

    def test_inheritance(self):
        """ Test for inheritance """
        self.assertTrue(issubclass(self.state1.__class__, BaseModel))

    def test_save_method(self):
        """ Test for save method """
        variable_update = self.state1.updated_at
        self.assertNotEqual(variable_update, self.state1.updated_at)
        self.state1.save()

    def test_attributes_consistency(self):
        """ Test for consistency of attributes """
        state1_json = self.state1.to_dict()
        self.state1.save()
        self.assertEqual(my_new_state.id, self.state1.id)
        my_new_state = State(**state1_json)
        self.assertEqual(my_new_state.created_at, self.state1.created_at)
        self.assertIsNot(self.state1, my_new_state)
        self.assertEqual(my_new_state.updated_at, self.state1.updated_at)

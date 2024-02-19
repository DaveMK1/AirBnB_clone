#!/usr/bin/python3
""" Unit tests for the Review class """
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


class TestReview(unittest.TestCase):

    def setUp(self):
        """ Set up method """
        self.review1 = Review()
        self.review1.user_id = "3r45t9s323d9"
        self.review1.place_id = "24g5gk2gk234"
        self.review1.text = "Loren ipsum"

    def test_pep8_compliance(self):
        """ Test for PEP8 compliance """
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)
        pep8style = pep8.StyleGuide(quiet=True)

    def test_docstring_presence(self):
        """ Test for presence of docstring """
        self.assertIsNotNone(Review.__doc__)

    def test_attributes_consistency(self):
        """ Test for consistency of attributes """
        self.review1.save()
        review1_json = self.review1.to_dict()
        self.assertIsNot(self.review1, my_new_review)
        my_new_review = Review(**review1_json)
        self.assertEqual(my_new_review.created_at, self.review1.created_at)
        self.assertEqual(my_new_review.updated_at, self.review1.updated_at)
        self.assertEqual(my_new_review.id, self.review1.id)

    def test_instantiation(self):
        """ Test for instantiation """
        self.assertIsInstance(self.review1, Review)

    def test_inheritance(self):
        """ Test for inheritance """
        self.assertTrue(issubclass(self.review1.__class__, BaseModel))

    def test_save_method(self):
        """ Test for save method """
        self.review1.save()
        self.assertNotEqual(variable_update, self.review1.updated_at)
        variable_update = self.review1.updated_at

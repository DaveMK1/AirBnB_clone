#!/usr/bin/python3
""" Unit tests for the BaseModel class """
import json
import unittest
import pep8
import os
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.engine.file_storage import FileStorage
from models.user import User
from models.review import Review

class TestBaseModel(unittest.TestCase):
    """ Test cases for the BaseModel class """

    def setUp(self):
        """ Set up method """
        self.bm_instance1 = BaseModel()
        self.bm_instance2 = BaseModel()

    def test_pep8_compliance(self):
        """ Test for PEP8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_instantiation(self):
        """ Test instantiation and types """
        self.assertIsInstance(self.bm_instance1, BaseModel)
        self.assertIsInstance(self.bm_instance1.created_at, datetime)
        self.assertIsInstance(self.bm_instance1.updated_at, datetime)

    def test_docstring_presence(self):
        """ Test for presence of docstrings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_id_generation(self):
        """ Test ID generation """
        self.assertNotEqual(self.bm_instance1.id, self.bm_instance2.id)
        self.assertTrue(hasattr(self.bm_instance1, "id"))
        self.assertEqual(type(self.bm_instance1.id), str)
        self.assertEqual(type(self.bm_instance2.id), str)

    def test_attributes_consistency(self):
        """ Test consistency of attributes """
        self.bm_instance1.name = "Holberton"
        self.bm_instance1.my_number = 89
        self.bm_instance1.save()
        bm_instance1_json = self.bm_instance1.to_dict()
        self.bm_instance2 = BaseModel(**bm_instance1_json)
        self.assertEqual(self.bm_instance2.id, self.bm_instance1.id)
        self.assertEqual(self.bm_instance2.name, self.bm_instance1.name)
        self.assertEqual(self.bm_instance2.my_number,
                self.bm_instance1.my_number)
        self.assertEqual(self.bm_instance2.created_at,
                self.bm_instance1.created_at)
        self.assertEqual(self.bm_instance2.updated_at,
                self.bm_instance1.updated_at)
        self.assertIsNot(self.bm_instance1, self.bm_instance2)

    def test_string_representation(self):
        """ Test string representation """
        bm_instance1_json = self.bm_instance1.to_dict()
        bm_instance3 = BaseModel(**bm_instance1_json)
        self.assertEqual(bm_instance3.__str__(),
                "[{}] ({}) {}".format(bm_instance3.__class__.__name__,
                    bm_instance3.id,
                    bm_instance3.__dict__))

    def test_save_method(self):
        """ Test save method """
        bm_instance1_json = self.bm_instance1.to_dict()
        bm_instance3 = BaseModel(**bm_instance1_json)
        self.bm_instance1.save()
        self.assertEqual(bm_instance3.created_at,
                self.bm_instance1.created_at)
        self.assertNotEqual(bm_instance3.updated_at,
                self.bm_instance1.updated_at)

    def test_dictionary_method(self):
        """ Test to_dict method """
        self.bm_instance1.name = "to infinity and beyond"
        self.assertIsInstance(bm1_dic, dict)
        self.assertEqual(bm1_dic['__class__'], "BaseModel")
        self.assertEqual(bm1_dic["id"], self.bm_instance1.id)
        update_aux = bm1_dic["updated_at"].split("T")
        self.assertEqual(" ".join(update_aux),
                str(self.bm_instance1.updated_at))

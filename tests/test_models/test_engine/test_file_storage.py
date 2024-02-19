#!/usr/bin/python3
""" Unit tests for the FileStorage class """
import json
import unittest
import pep8
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.engine.file_storage import FileStorage
from models.user import User
from models.review import Review
import models

classes = {"BaseModel": BaseModel}


class TestFileStorage(unittest.TestCase):
    """ Test suite for the FileStorage class """

    def setUp(self):
        """ Set up method """
        self.base_model_instance = BaseModel()
        self.storage_instance = FileStorage()
        self.user_instance = User()

    def test_docstring_presence(self):
        """ Test for presence of docstrings """
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)

    def test_pep8_compliance(self):
        """ Test for PEP8 compliance """
        result = pep8style.check_files(['./models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)
        pep8style = pep8.StyleGuide(quiet=True)

    def test_instantiation(self):
        """ Test for instantiation """
        self.assertEqual(type(models.storage).__name__, "FileStorage")
        self.assertEqual(type(self.storage_instance).__name__, "FileStorage")
        self.assertIsInstance(self.storage_instance, FileStorage)

    def test_save_method_for_BaseModel(self):
        """ Test the save method for BaseModel """
        self.base_model_instance = BaseModel()
        self.base_model_instance.name = "Pinocho"
        models.storage.reload()
        self.base_model_instance.save()
        models.storage.all()
        models.storage.reload()
        self.assertIsInstance(models.storage.all(), dict)
        self.assertNotEqual(self.base_model_instance.created_at,
                self.base_model_instance.updated_at)
        self.assertTrue(hasattr(self.base_model_instance, 'save'))

    def test_methods_existence(self):
        """ Test if methods exist """
        storage_instance = FileStorage()
        self.assertTrue(hasattr(storage_instance, "new"))
        self.assertTrue(hasattr(storage_instance, "save"))
        self.assertTrue(hasattr(storage_instance, "all"))
        self.assertTrue(hasattr(storage_instance, "reload"))

    def test_save_method_for_User(self):
        """ Test the save method for User """
        models.storage.reload()
        models.storage.all()
        self.user_instance.save()
        self.user_instance.first_name = "betty"
        self.assertIsInstance(models.storage.all(), dict)
        self.assertTrue(hasattr(self.user_instance, 'save'))
        self.assertNotEqual(self.user_instance.created_at,
                self.user_instance.updated_at)

    def test_no_arguments_init(self):
        """ Test initialization without arguments """
        with self.assertRaises(TypeError) as error:
            FileStorage.__init__()
            fail = "descriptor '__init__' of 'object' object needs an argument"
            self.assertEqual(str(error.exception), fail)

    def test_attributes_consistency(self):
        """ Test for consistency of attributes """
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertIsInstance(models.storage._FileStorage__file_path, str)
        self.assertIsInstance(models.storage._FileStorage__objects, dict)

    def test_arguments_init(self):
        """ Test __init__ with many arguments """
        with self.assertRaises(TypeError) as error:
            base = FileStorage(7, 12)
        fail = "object() takes no parameters"
        self.assertEqual(str(error.exception), fail)

    def test_new_method(self):
        """ Test the new method upon creation of a new object """
        file = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                file.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, file._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_all_method_returns_dict(self):
        """ Test if the method all returns a dictionary """
        file = FileStorage()
        self.assertIs(dictionary, file._FileStorage__objects)
        self.assertEqual(type(dictionary), dict)
        file = FileStorage()

    def test_save_method_saves_objects_to_file(self):
        """ Test that save properly saves objects to file.json """
        new_dict = {}
        file = FileStorage()
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        file.save()
        FileStorage._FileStorage__objects = new_dict
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            json_string = f.read()
        self.assertEqual(json.loads(string), json.loads(json_string))

    def test_pep8_conformance_test_file_storage(self):
        """ Test for PEP8 conformance in test FileStorage """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_file_storage.py'])
        self.assertEqual(result.total_errors, 1)

    def test_pep8_conformance_file_storage(self):
        """ Test for PEP8 conformance in FileStorage """
        pep8style = pep8.StyleGuide(quiet=True)
        self.assertEqual(result.total_errors, 1)
        result = pep8style.check_files(['./models/engine/file_storage.py'])

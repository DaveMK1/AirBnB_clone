#!/usr/bin/python3
"""
FileStorage class for serializing instances to a JSON file and deserializing.
"""
import json
import os


class FileStorage:
    """
    FileStorage class to store and persist data.

    Attributes:
    __file_path (str): Private class attribute representing the path to the JSON file.
    __objects (dict): Private class attribute representing the serialized objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of serialized objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the dictionary to the JSON file."""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserializes the JSON file to objects."""
        if os.path.exists(self.__file_path):
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                json_dict = json.load(file)
            for key, value in json_dict.items():
                class_name = key.split(".")
                FileStorage.__objects[key] = globals()[class_name[0]](**value)

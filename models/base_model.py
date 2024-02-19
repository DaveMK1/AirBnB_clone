#!/usr/bin/python3
"""
BaseModel class defines common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
import models
import json

ISO_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Base class for other classes to inherit from.

    Attributes:
    id (str): Public instance attribute for identification.
    created_at (datetime): Public instance attribute for creation time.
    updated_at (datetime): Public instance attribute for update time.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes object/instance attributes.

        Args:
        args: Variable length argument list.
        kwargs: Arbitrary keyword arguments.

        Attributes:
        id: Contains the object's identification.
        created_at: The datetime when the object was created.
        updated_at: The datetime when the object was modified.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, ISO_FORMAT))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.

        Returns:
        dict: A dictionary representation of the instance.
        """
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.strftime(ISO_FORMAT)
        dic['updated_at'] = self.updated_at.strftime(ISO_FORMAT)
        return dic

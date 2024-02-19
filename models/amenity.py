#!/usr/bin/python3
"""
Amenity class inheriting from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class, inherits BaseModel."""

    def __init__(self):
        """Initializing Amenity class."""
        super().__init__()
        name = ""

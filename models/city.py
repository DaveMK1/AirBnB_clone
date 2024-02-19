#!/usr/bin/python3
"""
City class inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel.

    Attributes:
    name (str): Public class attribute representing the city's name.
    state_id (str): Public class attribute representing the state's id.
    """

    name = ""
    state_id = ""

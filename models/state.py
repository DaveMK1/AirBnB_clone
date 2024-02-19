#!/usr/bin/python3
"""
State class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel.

    Attributes:
    name (str): Public class attribute representing the state's name.
    """

    name = ""

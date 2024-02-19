#!/usr/bin/python3
"""
User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel.

    Attributes:
    email (str): Public class attribute representing the user's email.
    password (str): Public class attribute representing the user's password.
    first_name (str): Public class attribute representing the user's first name.
    last_name (str): Public class attribute representing the user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

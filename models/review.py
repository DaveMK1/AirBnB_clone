#!/usr/bin/python3
"""
Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel.

    Attributes:
    text (str): Public class attribute representing the review text.
    place_id (str): Public class attribute representing the place's id.
    user_id (str): Public class attribute representing the user's id.
    """

    text = ""
    place_id = ""
    user_id = ""

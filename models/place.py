#!/usr/bin/python3
"""
Place class inherits from BaseModel.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherits from BaseModel.

    Attributes:
    city_id (str): Public class attribute representing the city's id.
    user_id (str): Public class attribute representing the user's id.
    name (str): Public class attribute representing the place's name.
    description (str): Public class attribute representing the place's description.
    number_rooms (int): Public class attribute representing the number of rooms.
    number_bathrooms (int): Public class attribute representing the number of bathrooms.
    max_guest (int): Public class attribute representing the maximum number of guests.
    price_by_night (int): Public class attribute representing the price per night.
    latitude (float): Public class attribute representing the latitude.
    longitude (float): Public class attribute representing the longitude.
    amenity_ids (list): Public class attribute representing the list of amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

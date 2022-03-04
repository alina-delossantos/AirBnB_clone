#!/usr/bin/python3
"""Place module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place
    Attributes:
        city_id (str): City ID.
        user_id (str): User ID.
        name (str): Place name.
        description (str): Place description.
        number_rooms (int): Nbr of rooms.
        number_bathrooms (int): Nbr of bathrooms.
        max_guest (int): Maximum Nbr of guests.
        price_by_night (int): Price per night.
        latitude (float): Latitude.
        longitude (float): Longitude.
        amenity_ids (list of str): List of amenities.
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

    def __init__(self, *args, **kwargs):
        """ Initialize class Place
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
                """
        super().__init__(*args, **kwargs)

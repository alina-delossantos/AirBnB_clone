#!/usr/bin/python3
"""Amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity
    Attributes:
        name (str): Amenity name.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize Amenity
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
        """
        super().__init__(*args, **kwargs)

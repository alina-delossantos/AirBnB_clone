#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City
    Attributes:
        state_id (str) State ID.
        name (str): City name.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize City
            Args:
                *args: list of strings
                **kwargs: dictionary of strings"""
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""State module"""
from models.base_model import BaseModel


class State(BaseModel):
    """class State
    Attributes:
        name (str): State name.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize class attributes
            Args:
                *args: list of strings
                **kwargs: dictionary of strings
        """
        super().__init__(*args, **kwargs)

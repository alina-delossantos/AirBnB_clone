#!/usr/bin/env python3
""" Creation of class base_model """
from unittest.loader import VALID_MODULE_NAME
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ BaseModel that defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        if kwargs:
            time = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, time))
                    continue
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return the instance's ID, class name, and attributes as a string"""

        return '[{}] ({}) {}'.format(
            type(self).__name__,
            self.id,
            str(self.__dict__)
        )

    def save(self):
        """ Save the object into .json file and updates the attribute
        'updated_at' with current time"""
        
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = type(self).__name__
        dictionar["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary


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

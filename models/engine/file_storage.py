#!/usr/bin/python3
"""Filestorage module serialises instance to JSON file"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """serialises and deserialises to JSON

    Arguments:
    __filepath (str): path to JSON file
    __objects (dict): obj dictionary
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """all method returns obj dictionary"""
        return self.__objects

    def new(self, obj):
        """adds obj to obj dict"""
        if obj:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialises objects to json file"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()

        json_str = json.dumps(obj_dict)

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json_str)

    def reload(self):
        """deserializes JSON file"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except FileNotFoundError:
            pass

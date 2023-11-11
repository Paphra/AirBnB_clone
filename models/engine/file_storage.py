#!/usr/bin/python3
"""file_storage module

Contains a class FileStorage for serialization and deserialization
- Saving to file and retriving
"""


import json
import os
from models import amenity
from models import base_model
from models import city
from models import place
from models import review
from models import state
from models import user


class FileStorage():
    """A class for serialization, deserialization and storing to file.
    """

    __file_path = 'file.json'
    __objects = {}
    __MODELS = {
        'BaseModel': base_model.BaseModel,
        'User': user.User,
        'Place': place.Place,
        'State': state.State,
        'City': city.City,
        'Amenity': amenity.Amenity,
        'Review': review.Review,
    }

    def __init__(self):
        """Initialize the file storage class
        """

        pass

    def all(self):
        """Returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """adds a new object

        Args:
            obj (object): a new object to add
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves the objects to a file
        """

        with open(self.__file_path, 'w') as file:
            json.dump(
                {k: v.to_dict() for k, v in self.__objects.items()},
                file
            )

    def reload(self):
        """Deserializes the JSON file to objects
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                objects = json.load(file).items()
                self.__objects = {
                    k: self.__MODELS[
                        k.split('.')[0]
                        ](**v) for k, v in list(objects)}

    def destroy(self, obj_key):
        """Delete an Object"""
        self.__objects.pop(obj_key)
        self.save()

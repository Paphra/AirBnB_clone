#!/usr/bin/python3
"""file_storage module

Contains a class FileStorage for serialization and deserialization
- Saving to file and retriving
"""


import json
import os


class FileStorage():
    """A class for serialization, deserialization and storing to file.
    """

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initialize the file storag class
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

        obj_dict = obj.to_dict()
        key = "{}.{}".format(obj_dict['__class__'], obj_dict['id'])
        self.__objects[key] = obj_dict

    def save(self):
        """Saves the objects to a file
        """

        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """Deserializes the JSON file to objects
        """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)

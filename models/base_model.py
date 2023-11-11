#!/usr/bin/python3
"""base_model module

Contains the BaseModel class
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """The Model from which all other models inherit
    """

    def __init__(self, *args, **kwargs):
        """The method that initializes properties

        Args:
            args (list): a list of positional arguments to the model
            kwargs (dict): a dictionary of all key word arguments
        """

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the Model
        """

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates the updated_at attr with current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Gets the dictionary containing all keys of __dict__

        Returns:
            dict: the dictionary containing all keys of the instance
        """

        ret_dict = {}       # dictionary to return
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                ret_dict[key] = datetime.isoformat(value)
            else:
                ret_dict[key] = value
        ret_dict['__class__'] = self.__class__.__name__

        return ret_dict

#!/usr/bin/python3
"""base_model module

Contains the BaseModel class
"""

import uuid
from datetime import datetime


class BaseModel():
    """The Model from which all other models inherit
    """

    def __init__(self):
        """The method that initializes properties
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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

    def to_dict(self):
        """Gets the dictionary containing all keys of __dict__

        Returns:
            dict: the dictionary containing all keys of the instance
        """

        ret_dict = {}       # dictionary to return
        for k, v in self.__dict__.items():
            if k in ['created_at', 'updated_at']:
                ret_dict[k] = datetime.isoformat(getattr(self, k))
            else:
                ret_dict[k] = v
        ret_dict['__class__'] = self.__class__.__name__

        return ret_dict

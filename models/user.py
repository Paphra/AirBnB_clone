#!/usr/bin/python3
"""user module

Contains the User class model
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class

    For creation of the User instance
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the user instance
        """
        super().__init__(self, *args, **kwargs)

#!/usr/bin/python3
"""review module

Contains the Review class model
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class

    For creation of the Review instances
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize the user instance
        """
        super().__init__(self, *args, **kwargs)

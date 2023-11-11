#!/usr/bin/python3
"""amenity module

Contains the Amenity class model
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class

    For creation of the Amenity instances
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the user instance
        """
        super().__init__(self, *args, **kwargs)

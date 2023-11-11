#!/usr/bin/python3
"""place module

Contains the Place class model
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class

    For creation of the Place instances
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    place_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize the user instance
        """
        super().__init__(self, *args, **kwargs)
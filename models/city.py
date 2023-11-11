#!/usr/bin/python3
"""city module

Contains the City class model
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class

    For creation of the City instances
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the user instance
        """
        super().__init__(self, *args, **kwargs)

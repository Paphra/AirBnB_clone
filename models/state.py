#!/usr/bin/python3
"""state module

Contains the State class model
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class

    For creation of the State instances
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the user instance
        """
        super().__init__(self, *args, **kwargs)

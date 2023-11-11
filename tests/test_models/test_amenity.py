#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import os
import re
import json
import time
from datetime import datetime
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.reset_storage()
        pass

    def reset_storage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        file_path = FileStorage._FileStorage__file_path
        if os.path.isfile(file_path):
            os.remove(file_path)

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""
        amenity_instance = Amenity()
        type_str = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(amenity_instance)), type_str)
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        amenity_instance = Amenity()
        for key, value in attributes.items():
            self.assertTrue(hasattr(amenity_instance, key))
            type_value = type(getattr(amenity_instance, key, None))
            self.assertEqual(type_value, value)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import os
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instantiation(self):
        """Tests instantiation of Amenity class."""
        amenity_instance = Amenity()
        type_str = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(amenity_instance)), type_str)
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))


if __name__ == "__main__":
    unittest.main()

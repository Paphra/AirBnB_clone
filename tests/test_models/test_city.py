#!/usr/bin/python3
"""test_city module

Contains tests for the City model
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """TestCase for the City model"""

    def setUp(self):
        """setup the test methods"""
        return super().setUp()

    def tearDown(self):
        """tear down all that was setup and tested"""
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

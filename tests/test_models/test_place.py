#!/usr/bin/python3
"""test_place module

Contains tests for the Place model
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestCase for the Place model"""

    def setUp(self):
        """setup the test methods"""
        return super().setUp()

    def tearDown(self):
        """tear down all that was setup and tested"""
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

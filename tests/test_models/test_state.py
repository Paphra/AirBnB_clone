#!/usr/bin/python3
"""test_state module

Contains tests for the State model
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """TestCase for the State model"""

    def setUp(self):
        """setup the test methods"""
        return super().setUp()

    def tearDown(self):
        """tear down all that was setup and tested"""
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

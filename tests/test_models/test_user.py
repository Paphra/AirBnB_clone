#!/usr/bin/python3
"""test_user module

Contains tests for the User model
"""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """TestCase for the User model"""

    def setUp(self):
        """setup the test methods"""
        return super().setUp()

    def tearDown(self):
        """tear down all that was setup and tested"""
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

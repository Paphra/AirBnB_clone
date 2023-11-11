#!/usr/bin/python3
"""test_review module

Contains tests for the Review model
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """TestCase for the Review model"""

    def setUp(self):
        """setup the test methods"""
        return super().setUp()

    def tearDown(self):
        """tear down all that was setup and tested"""
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

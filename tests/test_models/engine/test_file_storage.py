#!/usr/bin/python3
"""Testing the file storage module and class
"""

import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """CLass that tests the File Storage class
    """

    def setUp(self) -> None:
        """Set up the test cases
        """
        return super().setUp()

    def tearDown(self) -> None:
        """tear down the test cases
        """
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()

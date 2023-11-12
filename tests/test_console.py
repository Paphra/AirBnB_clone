#!/usr/bin/python3
"""test_console module

Contains the tests for the console command interpreter
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Testing class for the HBNBCommand
    """

    def setUp(self) -> None:
        """Setup the tests
        """
        return super().setUp()

    def tearDown(self) -> None:
        """Tear down the tests
        """
        return super().tearDown()

    def test_console_entry(self):
        """Test the entry to the console
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("? show")


if __name__ == "__main___":
    unittest.main()

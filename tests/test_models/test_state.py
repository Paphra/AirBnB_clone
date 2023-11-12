#!/usr/bin/python3
"""test_state module

Contains tests for the State model
"""

import unittest
import os
from importlib import reload
from models import base_model
from models import state
from models.engine import file_storage
from models import storage


class TestState(unittest.TestCase):
    """TestCase for the State model
    """

    __file = "file.json"

    def setUp(self):
        """setup the test methods
        """
        reload(base_model)
        reload(state)
        reload(file_storage)

        if os.path.exists(self.__file):
            os.remove(self.__file)
        storage._FileStorage__objects = {}

    def tearDown(self):
        """tear down all that was setup and tested
        """
        if os.path.exists(self.__file):
            os.remove(self.__file)
        storage._FileStorage__objects = {}

    def test_state_instantiation(self):
        """Testing the instantiation of the State model
        """

        from models.state import State
        from models.base_model import BaseModel

        s = State()
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(hasattr(s, 'id'))
        self.assertTrue(hasattr(s, 'created_at'))
        self.assertTrue(hasattr(s, 'updated_at'))
        self.assertTrue(hasattr(s, 'name'))
        self.assertEqual(type(s.name), str)
        self.assertEqual(s.name, "")

        m_attr = dir(s)
        self.assertTrue('save' in m_attr)
        s2 = State(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertNotEqual(s, s2)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)

    def test_state_file_storage_integration(self):
        """Tests the integration of file storage in the State model
        """
        from models.state import State

        s = State()
        s.name = "Wakiso"
        s.save()
        self.assertTrue(os.path.exists(self.__file))
        self.assertNotEqual(os.path.getsize(self.__file), 0)
        self.assertEqual(len(storage.all()), 1)
        key = "State.{}".format(s.id)
        self.assertEqual(storage.all()[key], s)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""test_city module

Contains tests for the City model
"""

import unittest
import os
from importlib import reload
from models import base_model
from models import city
from models.engine import file_storage
from models import storage


class TestCity(unittest.TestCase):
    """TestCase for the City model
    """

    __file = "file.json"

    def setUp(self):
        """setup the test methods
        """
        reload(base_model)
        reload(city)
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

    def test_city_instantiation(self):
        """Testing the instantiation of the City model
        """

        from models.city import City
        from models.base_model import BaseModel

        s = City()
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(hasattr(s, 'id'))
        self.assertTrue(hasattr(s, 'created_at'))
        self.assertTrue(hasattr(s, 'updated_at'))
        self.assertTrue(hasattr(s, 'name'))
        self.assertTrue(hasattr(s, 'state_id'))
        self.assertEqual(type(s.name), str)
        self.assertEqual(type(s.state_id), str)
        self.assertEqual(s.name, "")
        self.assertEqual(s.state_id, "")

        m_attr = dir(s)
        self.assertTrue('save' in m_attr)
        s2 = City(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertNotEqual(s, s2)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)

    def test_city_file_storage_integration(self):
        """Tests the integration of file storage in the City model
        """
        from models.city import City
        from models.state import State

        s = City()
        s.name = "Wakiso"
        s.save()
        self.assertTrue(os.path.exists(self.__file))
        self.assertNotEqual(os.path.getsize(self.__file), 0)
        self.assertEqual(len(storage.all()), 1)
        key = "City.{}".format(s.id)
        self.assertEqual(storage.all()[key], s)
        state = State()
        s.state_id = state.id


if __name__ == "__main__":
    unittest.main()

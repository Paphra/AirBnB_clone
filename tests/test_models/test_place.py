#!/usr/bin/python3
"""test_place module

Contains tests for the Place model
"""

import unittest
import os
from importlib import reload
from models import base_model
from models import place
from models.engine import file_storage
from models import storage


class TestPlace(unittest.TestCase):
    """TestCase for the Place model
    """

    __file = "file.json"

    def setUp(self):
        """setup the test methods
        """
        reload(base_model)
        reload(place)
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

    def test_place_instantiation(self):
        """Testing the instantiation of the Place model
        """

        from models.place import Place
        from models.base_model import BaseModel

        s = Place()
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(hasattr(s, 'id'))
        self.assertTrue(hasattr(s, 'created_at'))
        self.assertTrue(hasattr(s, 'updated_at'))
        self.assertTrue(hasattr(s, 'name'))
        self.assertTrue(hasattr(s, 'city_id'))
        self.assertTrue(hasattr(s, 'user_id'))
        self.assertTrue(hasattr(s, 'description'))
        self.assertTrue(hasattr(s, 'number_rooms'))
        self.assertTrue(hasattr(s, 'number_bathrooms'))
        self.assertTrue(hasattr(s, 'max_guest'))
        self.assertTrue(hasattr(s, 'price_by_night'))
        self.assertTrue(hasattr(s, 'latitude'))
        self.assertTrue(hasattr(s, 'longitude'))
        self.assertTrue(hasattr(s, 'amenity_ids'))
        self.assertEqual(type(s.name), str)
        self.assertEqual(type(s.user_id), str)
        self.assertEqual(type(s.city_id), str)
        self.assertEqual(type(s.description), str)
        self.assertEqual(type(s.number_rooms), int)
        self.assertEqual(type(s.number_bathrooms), int)
        self.assertEqual(type(s.max_guest), int)
        self.assertEqual(type(s.price_by_night), int)
        self.assertEqual(type(s.latitude), float)
        self.assertEqual(type(s.longitude), float)
        self.assertEqual(type(s.amenity_ids), list)
        self.assertEqual(s.name, "")

        m_attr = dir(s)
        self.assertTrue('save' in m_attr)
        s2 = Place(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertNotEqual(s, s2)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)

    def test_place_file_storage_integration(self):
        """Tests the integration of file storage in the Place model
        """
        from models.place import Place

        s = Place()
        s.name = "Wonderful Apartments"
        s.save()
        self.assertTrue(os.path.exists(self.__file))
        self.assertNotEqual(os.path.getsize(self.__file), 0)
        self.assertEqual(len(storage.all()), 1)
        key = "Place.{}".format(s.id)
        self.assertEqual(storage.all()[key], s)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""test_review module

Contains tests for the Review model
"""

import unittest
import os
from importlib import reload
from models import base_model
from models import review
from models.engine import file_storage
from models import storage


class TestReview(unittest.TestCase):
    """TestCase for the Review model
    """

    __file = "file.json"

    def setUp(self):
        """setup the test methods
        """
        reload(base_model)
        reload(review)
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

    def test_review_instantiation(self):
        """Testing the instantiation of the Review model
        """

        from models.review import Review
        from models.base_model import BaseModel

        s = Review()
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(hasattr(s, 'id'))
        self.assertTrue(hasattr(s, 'created_at'))
        self.assertTrue(hasattr(s, 'updated_at'))
        self.assertTrue(hasattr(s, 'text'))
        self.assertTrue(hasattr(s, 'place_id'))
        self.assertTrue(hasattr(s, 'user_id'))
        self.assertEqual(type(s.text), str)
        self.assertEqual(type(s.place_id), str)
        self.assertEqual(type(s.user_id), str)
        self.assertEqual(s.text, "")
        self.assertEqual(s.place_id, "")
        self.assertEqual(s.user_id, "")

        m_attr = dir(s)
        self.assertTrue('save' in m_attr)
        s2 = Review(**s.to_dict())
        self.assertEqual(s.id, s2.id)
        self.assertNotEqual(s, s2)
        self.assertEqual(s.created_at, s2.created_at)
        self.assertEqual(s.updated_at, s2.updated_at)

    def test_review_file_storage_integration(self):
        """Tests the integration of file storage in the Review model
        """
        from models.review import Review
        from models.place import Place
        from models.user import User

        s = Review()
        s.text = "Something interesting Yet to come"
        s.save()
        self.assertTrue(os.path.exists(self.__file))
        self.assertNotEqual(os.path.getsize(self.__file), 0)
        self.assertEqual(len(storage.all()), 1)
        key = "Review.{}".format(s.id)
        self.assertEqual(storage.all()[key], s)
        user = User()
        place = User()
        s.user_id = user.id
        s.place_id = place.id


if __name__ == "__main__":
    unittest.main()

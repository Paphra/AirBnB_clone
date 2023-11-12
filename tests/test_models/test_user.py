#!/usr/bin/python3
"""test_user module

Contains tests for the User model
"""

import unittest
import os
from importlib import reload
from models import base_model
from models import user
from models.engine import file_storage


class TestUser(unittest.TestCase):
    """TestCase for the User model"""

    __path = "file.json"

    def setUp(self):
        """setup the test methods
        """
        reload(base_model)
        reload(user)
        reload(file_storage)
        if os.path.exists(self.__path):
            os.remove(self.__path)

    def tearDown(self):
        """tear down all that was setup and tested
        """

        if os.path.exists(self.__path):
            os.remove(self.__path)

    def test_user_instantiation(self):
        """Testing the instantiation of the model of User
        """
        from models.user import User
        from models.base_model import BaseModel
        from models import storage

        u = User()
        self.assertTrue(issubclass(u.__class__, BaseModel))
        self.assertTrue(hasattr(u, 'id'))
        self.assertTrue(hasattr(u, 'created_at'))
        self.assertTrue(hasattr(u, 'updated_at'))
        self.assertTrue(hasattr(u, 'email'))
        self.assertTrue(hasattr(u, 'password'))
        self.assertTrue(hasattr(u, 'first_name'))
        self.assertTrue(hasattr(u, 'last_name'))
        self.assertEqual(type(u.email), str)
        self.assertEqual(type(u.password), str)
        self.assertEqual(type(u.last_name), str)
        self.assertEqual(type(u.first_name), str)
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

        u2 = User(**u.to_dict())
        self.assertEqual(u.id, u2.id)
        self.assertEqual(u.created_at, u2.created_at)
        self.assertEqual(u.updated_at, u2.updated_at)

    def test_user_file_storage_integration(self):
        """Test the integration of User model with the file storage
        """
        from models.user import User
        from models import storage

        u = User()

        u.first_name = "Epaphradito"
        u.last_name = "Lugayavu"
        u.email = "paphra.me@gmail.com"
        u.password = "roots"
        u.save()
        self.assertTrue(os.path.exists(self.__path))
        self.assertNotEqual(os.path.getsize(self.__path), 0)
        self.assertEqual(len(storage.all()), 1)
        key = "User.{}".format(u.id)
        self.assertEqual(storage.all()[key], u)


if __name__ == "__main__":
    unittest.main()

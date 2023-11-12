#!/usr/bin/python3
"""Testing the file storage module and class
"""

import unittest
import os
import json
from importlib import reload
from models.engine import file_storage
from models import base_model


class TestFileStorage(unittest.TestCase):
    """CLass that tests the File Storage class
    """

    __file_path = 'file.json'

    def setUp(self) -> None:
        """Set up the test cases
        """
        from models import storage

        if os.path.exists(self.__file_path):
            os.remove(self.__file_path)
        reload(file_storage)
        reload(base_model)
        storage._FileStorage__objects = {}

    def tearDown(self) -> None:
        """tear down the test cases
        """
        from models import storage

        if os.path.exists(self.__file_path):
            os.remove(self.__file_path)
        storage._FileStorage__objects = {}

    def test_file_storage_instantiation(self):
        """Test the instanciation of the File Storage class
        """

        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        self.assertFalse(hasattr(storage, 'file_path'))
        self.assertFalse(hasattr(storage, '__file_path'))
        self.assertFalse(hasattr(storage, '__objects'))
        self.assertTrue(type(storage._FileStorage__file_path), str)
        self.assertTrue(type(storage._FileStorage__objects), dict)
        self.assertFalse(os.path.exists(self.__file_path))
        self.assertEqual(storage._FileStorage__objects, {})
        self.assertGreater(storage._FileStorage__file_path, "")

    def test_file_storage_methods(self):
        """Check for the existence of the mehtods specified
        """
        from models.engine.file_storage import FileStorage
        from models.base_model import BaseModel

        storage = FileStorage()
        methods_attrs = dir(storage)
        self.assertTrue('all' in methods_attrs)
        self.assertTrue('new' in methods_attrs)
        self.assertTrue('save' in methods_attrs)
        self.assertTrue('reload' in methods_attrs)

        # return values and operations
        self.assertDictEqual(storage._FileStorage__objects, storage.all())
        self.assertDictEqual(storage.all(), {})
        bm = BaseModel()
        storage.new(bm)
        self.assertNotEqual(storage.all(), {})
        self.assertEqual(len(storage.all()), 1)
        storage.save()
        self.assertTrue(os.path.exists(self.__file_path))
        self.assertNotEqual(os.path.getsize(self.__file_path), 0)
        with open(self.__file_path, 'r') as file:
            contents = json.load(file)
            self.assertNotEqual(contents, storage.all())
        storage2 = FileStorage()
        self.assertNotEqual(storage2.all(), {})
        self.assertEqual(storage.all(), storage2.all())
        storage2.reload()
        self.assertNotEqual(storage2.all(), {})
        self.assertNotEqual(storage.all(), storage2.all())

    def test_base_model_file_storage_integration(self):
        """Test the integration of the file storage in base model
        """
        from models import storage

        bm = base_model.BaseModel()
        bm.name = "Epaphradito"
        bm.save()
        key = "BaseModel.{}".format(bm.id)
        self.assertDictEqual(
            storage._FileStorage__objects[key].to_dict(),
            bm.to_dict(),
        )
        bm_recreated = base_model.BaseModel(**bm.to_dict())
        self.assertEqual(bm.id, bm_recreated.id)
        self.assertNotEqual(bm, bm_recreated)
        self.assertEqual(len(storage.all()), 1)


if __name__ == "__main__":
    unittest.main()

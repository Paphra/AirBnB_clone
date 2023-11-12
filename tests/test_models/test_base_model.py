#!/usr/bin/python3
"""Testing the BaseModel class"""

import unittest
from importlib import reload
from models import base_model
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test of Base Model class"""

    def setUp(self) -> None:
        """Setup the tests for the base model
        """
        reload(base_model)

    def test_base_model_instantiation(self):
        """Test instance of BaseClass class"""
        from models.base_model import BaseModel

        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1, bm2)
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertEqual(type(bm1.id), str)
        self.assertTrue(hasattr(bm1, 'created_at'))
        self.assertTrue(hasattr(bm1, 'updated_at'))
        self.assertEqual(type(bm2.created_at), datetime)
        self.assertEqual(type(bm2.updated_at), datetime)

    def test_base_model_instantiation_with_kwargs(self):
        """Testing the base mode instantiation
        """
        from models.base_model import BaseModel

        bm1 = BaseModel(
            id="123",
            created_at="2021-02-17T22:46:38.883036",
            updated_at="2021-02-17T22:46:38.883036")
        bm2 = BaseModel(id="123", name="Matias tu papi")
        self.assertEqual(bm1.id, "123")
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_base_model_documentation(self):
        """Check documentation
        """
        from models.base_model import BaseModel

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_base_model_str_method(self):
        """Test method str"""
        from models.base_model import BaseModel

        bm = BaseModel()
        self.assertEqual(
            str(bm),
            "[{}] ({}) {}".format(
                'BaseModel',
                bm.id,
                bm.__dict__))

    def test_base_model_to_dict_method(self):
        """ Tests to_dict method """
        from models.base_model import BaseModel

        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertNotEqual(bm.__dict__, bm_dict)
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)
        self.assertTrue("__class__" in bm_dict)
        self.assertEqual(bm_dict["__class__"], "BaseModel")

    def test_base_model_save_mthod(self):
        """Tests for save function
        """
        from models.base_model import BaseModel

        bm = BaseModel()
        created_at = bm.created_at
        updated_at = bm.updated_at
        bm.save()
        updated_at_update = bm.updated_at
        self.assertNotEqual(updated_at, updated_at_update)
        self.assertGreater(updated_at_update, updated_at)


if __name__ == "__main__":
    unittest.main()

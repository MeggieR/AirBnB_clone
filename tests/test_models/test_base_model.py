import unittest
from datetime import datetime
from time import sleep
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def test_initialization(self):
        """Test that a new BaseModel instance is initialized correctly."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_str(self):
        """Test the __str__ method."""
        model = BaseModel()
        expected_str = "[{}] ({}) {}".format(model.__class__.__name__, model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Test the save method updates the updated_at attribute."""
        model = BaseModel()
        original_updated_at = model.updated_at
        sleep(1)  # Sleep for a second to ensure a time difference
        model.save()
        self.assertNotEqual(model.updated_at, original_updated_at)
        self.assertGreater(model.updated_at, original_updated_at)

    def test_to_dict(self):
        """Test the to_dict method returns the correct dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()


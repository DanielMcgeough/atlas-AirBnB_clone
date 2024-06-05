#!/usr/bin/python3


import datetime
import unittest
import models
from unittest.mock import MagicMock
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.b1 = models.base_model.BaseModel()

    def tearDown(self):
        del self.b1

    def test_save(self):
        dummy_updated_at = self.b1.updated_at

        self.b1.save()

        self.assertNotEqual(self.b1.updated_at, dummy_updated_at)
        self.assertIsInstance(self.b1.updated_at, datetime.datetime)

    def test_to_dict(self):
        self.assertTrue(isinstance(self.b1.to_dict(), dict))

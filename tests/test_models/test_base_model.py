#!/usr/bin/python3


import datetime
import unittest
import models
import json
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.b1 = models.base_model.BaseModel()

    def tearDown(self):
        del self.b1

    def test_save(self):
        dummy_updated_at = self.b1.updated_at

        self.b1.save()

        key = "BaseModel" + "." + self.b1.id

        with open('file.json', 'r') as file:
            self.assertEqual(
                    json.load(file)[key],
                    self.b1.to_dict())

    def test_todict(self):
        self.assertTrue(isinstance(self.b1.to_dict(), dict))

#!/usr/bin/python3


import unittest
import models


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.b1 = models.base_model.BaseModel()

    def tearDown(self):
        del self.b1

    def test_save(self):
        self.assertTrue(hasattr(self.b1, 'save'))

    def test_to_dict(self):
        self.assertTrue(isinstance(self.b1.to_dict(), dict))

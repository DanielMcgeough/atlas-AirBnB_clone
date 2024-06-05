#!/usr/bin/python3
"""
Unittests for models.city
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unittest for instances of City
    """

    def setUp(self):
        self.c1 = City()

    def tearDown(self):
        del self.c1

    def test_bare_minimum_instancing(self):
        self.assertEqual(City, type(City()))

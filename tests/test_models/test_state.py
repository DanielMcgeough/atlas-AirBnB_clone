#!/usr/bin/python3
"""
Unittests for models.state
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """
    Unittest for instances of State
    """

    def setUp(self):
        self.s1 = State()

    def tearDown(self):
        del self.s1

    def test_bare_minimum_instancing(self):
        self.assertEqual(Amenity, type(Amenity()))

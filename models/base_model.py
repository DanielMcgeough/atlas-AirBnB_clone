#!/usr/bin/python3
"""This defines the class called BaseModel"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents BaseModel class for AirBnB project"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance
        Args:
            *args - a tuple
            **kwargs - a dictionary
        """
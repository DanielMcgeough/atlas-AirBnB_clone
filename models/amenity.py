#!/usr/bin/python3
"""
This Defines the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This represents an amenity.
    Attributes:
        name (str): The name of the amenity.
    """
    name = ""

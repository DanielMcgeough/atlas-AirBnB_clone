#!/usr/bin/python3
"""
This Defines the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""

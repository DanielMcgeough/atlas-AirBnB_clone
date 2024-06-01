#!/usr/bin/python3
"""
This defines the state class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This represents a state.
    Attributes:
        name (str): The name of the state.
    """

    name = ""

#!/usr/bin/python3
"""
This defines the city class
"""
import models.base_model import BaseModel


class City(BaseModel):
    """
    This represents a city
    
    Attributes:
        state_id (str): the state id.
        name (str): the name of the city.
    """
    state_id= ""
    name= ""

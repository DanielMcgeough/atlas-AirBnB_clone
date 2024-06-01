#!/usr/bin/python3
"""
This defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User.
    Attributes:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The email address of the user.
        password (str): The password of the user.
    """

    first_name = ""
    last_name = ""
    email = ""
    password = ""

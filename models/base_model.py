#!/usr/bin/python3

import models
import datetime
import uuid


class BaseModel():
    """
    This Class represents the BaseModel
    of the AirBnB project
    """
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel
        Args:
            *args (Tuple)
            **kwargs (dict)
        """
        if (kwargs):
            for argkey, argval in kwargs.items():
                if argkey != '__class__':
                    if argkey == 'created_at' or argkey == 'updated_at':
                        argval = datetime.datetime.fromisoformat(argval)
                    setattr(self, argkey, argval)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return the print/str
        representation
        of the BaseModel instance
        """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Update updated_at with
        the current datetime."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of
        the BaseModel instance."""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy

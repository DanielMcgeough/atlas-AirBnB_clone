#!/usr/bin/python3

import models
import datetime
import uuid

class BaseModel():

    def __init__(self, *args, **kwargs):

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

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__

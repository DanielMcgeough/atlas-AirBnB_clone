#!/usr/bin/python3


import json
from models.base_model import BaseModel


class FileStorage():

    def __init__(self, file_path, objects):
        """
        Initialize a new FileStorage instance
        Args:
            file_path (string)
            objects (unknown type)
        """
        self.__file_path = file_path
        self.__objects = objects
        self.classes = {"BaseModel": BaseModel}

    def all(self):
        """
        Returns all of the objects
        currently available to be stored
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        Saves all objects in __objects dictionary
        using JSON to a .json file
        """
        objects = {}
        for key in self.__objects:
            objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(objects, file)

    def reload(self):
        """
        Loads objects from a .json file using
        JSON to the __objects dictionary
        """
        try:
            with open(self.__file_path, "r") as file:
                json_instances = json.load(file)
                for key, obj in json_instances.items():
                    self.__objects[key] = self.classes[obj["__class__"]](**obj)

        except FileNotFoundError:
            pass

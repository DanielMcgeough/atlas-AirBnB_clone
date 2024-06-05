#!/usr/bin/python3
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import json
from models.base_model import BaseModel


class FileStorage():

    def __init__(self):
        """
        Initialize a new FileStorage instance
        Args:
            file_path (string)
            objects (unknown type)
        """
        self.__file_path = 'file.json'
        self.__objects = {}
        self.__classes = {
                "Amenity": Amenity,
                "BaseModel": BaseModel,
                "City": City,
                "Place": Place,
                "Review": Review,
                "State": State,
                "User": User
                }

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
                    self.__objects[key] = self.__classes[obj["__class__"]](**obj)

        except FileNotFoundError:
            pass

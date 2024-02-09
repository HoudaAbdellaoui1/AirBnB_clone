#!/usr/bin/python3
import json
from os import path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Class for serializing instances to a JSON file
    and deserializing JSON file to instances."""

    __file_path = "file.json"
    __objects = {}
    # __classDictionary = {
    #     "User": User,
    #     "State": State,
    #     "City": City,
    #     "Amenity": Amenity,
    #     "Place": Place,
    #     "Review": Review
    # }
    __classDictionary = {
        "User": User,
    }

    def all(self, cl=None):
        """Returns the dictionary __objects."""
        cl = cl if not isinstance(cl, str) else self.__clsdict.get(cl)
        if cl:
            return {k: v for k, v in self.__objects.items()
                    if isinstance(v, cl)}
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict()
                              for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    # def reload(self):
    #     """
    #     Deserializes the JSON file to __objects.

    #     If the JSON file exists, it loads the data into __objects.
    #     Otherwise, do nothing.
    #     """
    #     try:
    #         with open(self.__file_path, 'r', encoding="UTF-8") as f:
    #             for key, value in (json.load(f)).items():
    #                 value = eval(value["__class__"])(**value)
    #                 self.__objects[key] = value
    #     except FileNotFoundError:
    #         pass

    def reload(self):
            """
            Deserializes the JSON file to __objects.

            If the JSON file exists, it loads the data into __objects.
            Otherwise, do nothing.
            """
            try:
                with open(self.__file_path, 'r', encoding="UTF-8") as f:
                    serialized_objects = json.load(f)
                    for key, value in serialized_objects.items():
                        class_name = value["__class__"]
                        cls = self.__classDictionary.get(class_name)
                        if cls:
                            obj = cls(**value)
                            self.__objects[key] = obj
            except FileNotFoundError:
                pass

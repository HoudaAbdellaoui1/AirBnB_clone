#!/usr/bin/python3
import json
from os import path



class FileStorage:
    """Class for serializing instances to a JSON file and deserializing JSON file to instances."""

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.

        If the JSON file exists, it loads the data into __objects.
        Otherwise, do nothing.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, obj_data in data.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create an instance of the class based on class name
                    cls = globals()[class_name]
                    # Create an instance of the class and initialize its attributes
                    obj_instance = cls(**obj_data)
                    self.__objects[key] = obj_instance

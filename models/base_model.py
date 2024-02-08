#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """A base model class providing common attributes and methods.

     Attributes:
        id: unique ID
        created_at: creation time
        updated_at: update time
    """
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    
    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel.
        Args:
            args: unused param
            kwargs: arguments for BaseModel constructor
        Attributes:
            id: unique id generated
            created_at: creation date
            updated_at: updated date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        if not self.id:
            self.id = str(uuid.uuid4())
        d = datetime.now()
        if not self.created_at:
            self.created_at = self.updated_at = d
        if not self.updated_at:
            self.updated_at = d

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the object attributes to a dictionary.

        Returns:
            dict: Dictionary containing object attributes.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = str(type(self).__name__)
        # Convert datetime objects to ISO format strings
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        if dict_copy.get('_sa_instance_state'):
            del dict_copy['_sa_instance_state']
        return dict_copy

    def __str__(self):
        """
        Generate a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

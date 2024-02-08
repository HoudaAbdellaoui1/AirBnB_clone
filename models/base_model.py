#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """A base model class providing common attributes and methods."""

    def __init__(self):
        """Initialize a new instance of BaseModel."""
        self.id = str(uuid.uuid4())  # Assign a unique ID
        self.created_at = datetime.now()  # Set creation time
        self.updated_at = datetime.now()  # Set update time

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
        # Convert datetime objects to ISO format strings
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        """
        Generate a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

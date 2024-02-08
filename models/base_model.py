import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            args: Unused.
            kwargs: A dictionary of keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel.

        Returns:
            A string with the format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation with “simple object type” of our BaseModel.

        Returns:
            A dictionary containing all keys/values of __dict__ of the instance.
            The keys are the attribute names of the instance and the values are
            the corresponding attribute values.
            A key __class__ must be added to this dictionary with the class name of the object.
            The created_at and updated_at must be converted to string object in ISO format.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
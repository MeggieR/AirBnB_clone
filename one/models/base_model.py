import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def __str__(self):
        """Returns string representation of the object"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        dict_json = self.__dict__.copy()
        dict_json['__class__'] = self.__class__.__name__
        dict_json['created_at'] = dict_json['created_at'].isoformat()
        dict_json['updated_at'] = dict_json['updated_at'].isoformat()
        return dict_json

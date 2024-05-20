import json
import os
from models.base_model import BaseModel

class FileStorage:
    """Class for serializing and deserializing `BaseModel` objects to and from a file."""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """Adds a new object to the storage."""
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """Returns a dictionary of all objects."""
        return FileStorage.__objects

    def save(self):
        """Serializes the objects to JSON and saves them to a file."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to objects if the file exists."""
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)  # Assuming classes are defined in the same module
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
            except Exception:
                pass

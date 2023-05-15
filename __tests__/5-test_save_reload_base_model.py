#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.save()
print(my_model)

print("-- Create a new object --")
my_model = User()
my_model.name = "Ozil"
my_model.my_number = 10
my_model.save()
print(my_model)

print("-- Create a new object --")
my_model = Amenity()
my_model.name = "Emirates"
my_model.save()
print(my_model)

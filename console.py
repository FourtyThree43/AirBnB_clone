#!/usr/bin/python3
"""Defines a Module for the HBNBCommand"""

import cmd
import importlib
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '
    __class_names = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, line):
        print("defualt(%s)" % line)
        return cmd.Cmd.default(self, line)

    def do_greet(self, line) -> None:
        '''Pints a greet message
        '''
        print("Hello")

    def do_quit(self, line) -> bool:
        """Quit: command to exit the program
        """
        return True

    def do_EOF(self, line) -> bool:
        """EOF: end-of-file mark the exits the program
        """
        "Exit"
        return True

    def emptyline(self) -> None:
        """Deals with the empty lines
        """
        pass

    def do_create(self, line) -> None:
        """
        Creates a new instance of BaseModel, saves it (JSON file) & prints id
        Usage: create <class name>
        Ex: $ create BaseModel
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in self.__class_names:
                print("** class doesn't exist **")
            else:
                try:
                    module_name = BaseModel.__module__
                    module = importlib.import_module(module_name)
                    cls = getattr(module, class_name)
                except AttributeError:
                    print("** class doesn't exist **")
                    return

                new_obj = cls()
                new_obj.save()
                print(new_obj.id)

    def do_show(self, line) -> None:
        """
        Prints the string rep. of an instance based on the class name & id.
        Usage: show <class name> <id>
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            obj_key = "{}.{}".format(args[0], args[1])
            obj = obj_dict.get(obj_key, None)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, line) -> None:
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage: destroy <class name> <id>
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            obj_key = "{}.{}".format(args[0], args[1])
            obj = obj_dict.get(obj_key, None)
            if obj is None:
                print("** no instance found **")
            else:
                obj_dict.pop(obj_key)
                storage.save()
                return

    def do_all(self, line) -> None:
        """
        Prints all string rep. of all instances based or not on the class name
        Usage: all <class name>
        Ex: $ all BaseModel or $ all.
        """
        args = line.split()

        if len(args) > 0 and args[0] not in self.__class_names:
            print("** class doesn't exist **")
        else:
            obj_list = []
            obj_dict = storage.all()
            if len(args) == 0 or args[0] in self.__class_names:
                for obj in obj_dict.values():
                    if len(args) == 0 or obj.__class__.__name__ == args[0]:
                        obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, line) -> None:
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = line.split()
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class_names:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            obj = obj_dict.get(obj_key, None)
            attr_name = args[2]
            attr_value = " ".join.args[3:]

            setattr(obj, attr_name, attr_value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

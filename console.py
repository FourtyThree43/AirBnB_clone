#!/usr/bin/python3
"""Defines a Module for the HBNBCommand"""

import cmd
import os
import importlib
import inspect
import pkgutil
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

    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes a new instance of HBNBCommand class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            __class_names (dict): Dictionary containing the names of the
                classes that inherit from BaseModel and their respective
                module names.
        """
        super().__init__(*args, **kwargs)
        self.__class_names = self.get_class_names()

    def get_class_names(self):
        """
        Dynamically discover class names that inherit from BaseModel.
        """
        class_names = {}
        for _, file_name, _ in pkgutil.iter_modules(['models']):
            module_name = os.path.splitext(file_name)[0]
            module = importlib.import_module('models.' + module_name)

            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, BaseModel):
                    class_names[name] = 'models.' + module_name
        return class_names

    def default(self, line):
        """Process a command line based on predefined syntax.

        This method parses the given command line and executes the
        corresponding command based on the syntax rules.

        Usage: <class name>.<command name>(<arg1>, <arg2>, ...)

        """
        cmd_dict: dict = {"all": self.do_all,
                          "count": self.do_count,
                          "show": self.do_show,
                          "destroy": self.do_destroy,
                          "update": self.do_update,
                          "create": self.do_create}
        parts = line.split(".")

        if len(parts) == 2 and parts[0] in self.__class_names:
            class_name = parts[0]
            rest_parts = parts[1].split("(")

            if len(rest_parts) == 2 and rest_parts[0] in cmd_dict:
                cmd_name = rest_parts[0]
                arg_str = rest_parts[1].rstrip(")")
                args = [class_name] + arg_str.split(",")
                cmd_str = " ".join(args)
                return cmd_dict[cmd_name](cmd_str)
            else:
                print("*** Unknown Syntax {}".format(line))

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
        Usage: create <class name>

        Creates a new instance of BaseModel, saves it (JSON file) & prints id

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
                    module_name = self.__class_names[class_name]
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
        Usage: show <class name> <id>

        Prints the string rep. of an instance based on the class name & id.

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
        Usage: destroy <class name> <id>

        Deletes an instance based on the class name and id
        (save the change into the JSON file).

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
        Usage: all <class name>

        Prints all string rep. of all instances based or not on the class name

        Ex: $ all BaseModel or $ all.
        """
        args = line.split()

        if len(args) > 0 and args[0] not in self.__class_names:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(args) == 0 or obj.__class__.__name__ == args[0]:
                    obj_list.append(obj.__str__())
            if len(obj_list) == 0:
                print("[]")
            else:
                print("[{}]".format(", ".join(obj_list)))

    def do_update(self, line) -> None:
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Updates an instance based on the class name and id by adding or
        updating attribute(name & value) or using a dictionary representation
        save the change into the JSON file)

        Example:
        $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        $ update User 1234-1234-1234-1234 {'first_name': 'John', 'age': 89}
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
            attr_value = args[3]

            try:
                if attr_value.isdigit():
                   attr_value = int(attr_value)
                elif float(attr_value):
                    attr_value = float(attr_value)
            except ValueError:
                pass

            class_attr = type(obj).__dict__
            if attr_name in class_attr.keys():
                try:
                    attr_value = type(class_attr[attr_name])(attr_value)
                except Exception:
                    print(f"** value type error: {attr_name} **")
                    print(f"Got: {type(attr_value)}")
                    print(f"Expected: {type(class_attr[attr_name])}")
                    return

            setattr(obj, attr_name, attr_value)
            storage.save()

    def do_count(self, line):
        """
        Usage: count <class_name>

        Count the number of instances of a given class.

        Ex: $ count BaseModel or $ count User
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == args[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

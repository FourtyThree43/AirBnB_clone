#!/usr/bin/python3
"""Defines a Module for the HBNBCommand"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_greet(self, line):
        '''Pints a greet message
        '''
        print("Hello")

    def do_quit(self, line):
        """Quit: command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF: end-of-file mark the exits the program
        """
        "Exit"
        return True

    def emptyline(self):
        """Deals with the empty lines
        """
        pass

    def parseline(self, line):
        print('parseline(%s) =>' % line)
        ret = cmd.Cmd.parseline(self, line)
        print(ret)
        return ret

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (JSON file) & prints id
        Ex: $ create BaseModel
        """
        pass

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        & id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        pass

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        pass

    def do_all(self, line):
        """
        Prints all string representation of all instances based or
        not on the class name.
        Ex: $ all BaseModel or $ all.
        """
        pass

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

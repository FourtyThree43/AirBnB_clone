#!/usr/bin/python3
"""Difines a Module for the HBNBCommand"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

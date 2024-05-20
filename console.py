#!/usr/bin/python3
"""
This module contains the HBNBCommand class, which provides a command-line interface for the HBNB project.
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class defines a command-line interpreter for the HBNB project.
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit command to exit the program, Usage: quit
        """
        return True

    def help_quit(self, arg):
        """
        Prints the help information for the quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        EOF command to exit the program, Usage: Ctrl-D
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()


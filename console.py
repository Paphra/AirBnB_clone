#!/usr/bin/python3
"""console module
"""

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The HBnB Console Application Class

    Args:
        cmd (Cmd): the command prompt
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the console
        """

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """

        return True

    def emptyline(self):
        '''To be called when an Empty line is Entered
        '''

        print('', end='')


if __name__ == '__main__':
    HBNBCommand().cmdloop()

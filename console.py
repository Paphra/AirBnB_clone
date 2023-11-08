#!/usr/bin/python3
"""console module
"""

import cmd


class Console(cmd.Cmd):
    """The Console Application Class

    Args:
        cmd (Cmd): the command prompt
    """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """End of File Method

        Returns:
            bool: always returns True
        """

        return True

    def do_quit(self, line):
        """Exit the Console application

        Returns:
            bool: always return True
        """

        return True

    def emptyline(self):
        '''To be called when an Empty line is Entered'''

        print('', end='')


if __name__ == '__main__':
    Console().cmdloop()

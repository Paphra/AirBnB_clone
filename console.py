#!/usr/bin/python3
"""console module
"""

import cmd
from models.base_model import BaseModel


class Console(cmd.Cmd):
    """The Console Application Class

    Args:
        cmd (Cmd): the command prompt
    """

    prompt = "(hbnb) "

    def do_test_base_task_3(self, line):
        """Test the BaseModel class
        """

        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(
                key,
                type(my_model_json[key]),
                my_model_json[key]))

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

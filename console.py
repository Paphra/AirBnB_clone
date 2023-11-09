#!/usr/bin/python3
"""console module
"""

import cmd
from models import storage
from models.base_model import BaseModel


class Console(cmd.Cmd):
    """The Console Application Class

    Args:
        cmd (Cmd): the command prompt
    """

    prompt = "(hbnb) "
    _TESTS = (
        'test_base_model',
        'test_base_model_dict',
        'test_save_reload_base_model'
    )

    def complete_test(self, text, line, begidx, endidx):
        """Complete commands
        """

        return [i for i in self._TESTS if i.startswith(text)]

    def do_test_base_model(self, line):
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

    def do_test_base_model_dict(self, line):
        """Test the BaseModel initialization
        """

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        print(my_model.id)
        print(my_model)
        print(type(my_model.created_at))
        print("--")
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(
                key,
                type(my_model_json[key]),
                my_model_json[key]))

        print("--")
        my_new_model = BaseModel(**my_model_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))

        print("--")
        print(my_model is my_new_model)

    def do_test_save_reload_base_model(self, line):
        """Test the saving a reloading methods of the storage class
        """

        all_objs = storage.all()
        print("-- Reloaded objects --")
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            print(obj)

        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        print(my_model)

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

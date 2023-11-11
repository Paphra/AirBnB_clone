#!/usr/bin/python3
"""console module
"""

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """The HBnB Console Application Class

    Args:
        cmd (Cmd): the command prompt
    """

    prompt = "(hbnb) "
    __MODELS = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review,
    }

    def do_EOF(self, line):
        """Exit the console
        """

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """

        return True

    def emptyline(self):
        """To be called when an Empty line is Entered
        """

        print('', end='')

    def class_name_missing(self):
        """Print ** class name missing **"""
        print("** class name missing **")

    def class_does_not_exist(self):
        """Print ** class doesn't exist **"""
        print("** class doesn't exist **")

    def instance_id_missing(self):
        """Print ** instance id missing **"""
        print("** instance id missing **")

    def no_instance_found(self):
        """Print ** no instance found **"""
        print("** no instance found **")

    def get_item(self, name, id):
        """Get the item"""

        obj_key = "{}.{}".format(name, id)
        storage.reload()
        objs = storage.all()
        item = objs.get(obj_key, False)

        return item

    def do_create(self, line):
        """Creates a new instance

        Saves it to the JSON file and prints the id
        """
        args = line.split()
        if len(args) < 1:
            self.class_name_missing()
        else:
            Model = self.__MODELS.get(args[0], False)
            if Model:
                item = Model()
                item.save()
                print(item)
            else:
                self.class_does_not_exist()

    def do_show(self, line):
        """Prints the string representation of an instance

        Based on class name and id
        """
        args = line.split()
        if len(args) < 1:
            self.class_name_missing()
        elif len(args) < 2:
            self.instance_id_missing()
        else:
            class_name = args[0]
            instance_id = args[1]
            Model = self.__MODELS.get(class_name, False)
            if Model:
                item = self.get_item(class_name, instance_id)
                if item:
                    print(item)
                else:
                    self.no_instance_found()
            else:
                self.class_does_not_exist()

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        if len(args) < 1:
            self.class_name_missing()
        elif len(args) < 2:
            self.instance_id_missing()
        else:
            class_name = args[0]
            instance_id = args[1]
            Model = self.__MODELS.get(class_name, False)
            if Model:
                item = self.get_item(class_name, instance_id)
                if item:
                    obj_key = "{}.{}".format(
                        item['__class__'], item['id']
                    )
                    storage.destroy(obj_key)
                else:
                    self.no_instance_found()
            else:
                self.class_does_not_exist()

    def do_all(self, line):
        """Prints all the string representation of all the instances
        """
        args = line.split()

        storage.reload()
        objs = storage.all()
        if len(args) < 1:
            all_objs = []
            for obj_key, obj in list(objs.items()):
                all_objs.append(str(obj))
            print(all_objs)
        else:
            Model = self.__MODELS.get(args[0], False)
            if Model:
                model_objs = []
                for obj_key, obj in list(objs.items()):
                    if obj_key.startswith(args[0]):
                        model_objs.append(str(obj))
                print(model_objs)
            else:
                self.class_does_not_exist()

    def do_update(self, line):
        """Updates an instance based on the class name and id"""

        args = line.split()
        if len(args) < 1:
            self.class_name_missing()
        elif len(args) < 2:
            self.instance_id_missing()
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]

            Model = self.__MODELS.get(class_name, False)
            if Model:
                item = self.get_item(class_name, instance_id)
                if item:
                    exclude = ['id', 'created_at', 'updated_at']
                    if attribute_name not in exclude:
                        setattr(
                            item,
                            attribute_name,
                            json.loads(attribute_value))
                        storage.new(item)
                        item.save()
                else:
                    self.no_instance_found()
            else:
                self.class_does_not_exist()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

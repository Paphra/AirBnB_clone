#!/usr/bin/python3
"""console module
"""

import cmd
import json
import re
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        pass

    def precmd(self, line: str):
        segs = line.split('.')
        if len(segs) == 2 and segs[0] in self.__MODELS.keys():
            class_name = segs[0]
            command_text = segs[1].replace("'", '"')
            if command_text in ['all()', 'count()']:
                command = command_text[:-2]
                line = "{} {}".format(command, class_name)
            elif command_text.startswith(('show', 'destroy')):
                ctl = command_text.split('("')
                if len(ctl) == 2 and ctl[1].endswith('")'):
                    command = ctl[0]
                    id = ctl[1][:-2]
                    line = "{} {} {}".format(
                        command,
                        class_name,
                        id
                    )
            elif command_text.startswith('update'):
                command = 'update'
                if command_text.endswith('})'):
                    b1 = command_text.find('(')
                    comma = command_text.find(',')
                    b2 = command_text.find(')')
                    instance_id = json.loads(
                        command_text[(b1 + 1):comma])
                    obj_update = json.loads(
                        command_text[(comma + 1):b2].strip())
                    count = 0
                    for k, v in list(obj_update.items()):
                        line = "{} {} {} {}".format(
                            class_name, instance_id, k, json.dumps(v)
                        )
                        if count < len(obj_update.items()) - 1:
                            self.do_update(line)
                        line = "update {}".format(line)

                elif command_text.endswith(')'):
                    ctl_tmp = command_text.split('(')
                    ctl = ctl_tmp[1][:-1].replace("'", '"')
                    ctl_array = ctl.split(',')
                    if len(ctl_array) == 3:
                        instance_id = json.loads(ctl_array[0])
                        attr = json.loads(ctl_array[1])
                        val = json.loads(ctl_array[2])

                        line = "{cmd} {cls} {id} {attr} {val}".format(
                            cmd=command,
                            cls=class_name,
                            id=instance_id,
                            attr=attr,
                            val=val
                        )

        return super().precmd(line)

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
                print(item.id)
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
                        class_name, item.id
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
                            attribute_value)
                        storage.new(item)
                        item.save()
                else:
                    self.no_instance_found()
            else:
                self.class_does_not_exist()

    def do_count(self, line):
        """Prints the number of items for a given instance
        """
        args = line.split()

        storage.reload()
        objs = storage.all()
        if len(args) < 1:
            self.class_name_missing()
        else:
            Model = self.__MODELS.get(args[0], False)
            if Model:
                model_objs = []
                for obj_key, obj in list(objs.items()):
                    if obj_key.startswith(args[0]):
                        model_objs.append(obj)
                print(len(model_objs))
            else:
                self.class_does_not_exist()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

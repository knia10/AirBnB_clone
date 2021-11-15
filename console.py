#!/usr/bin/python3

"""
console.py that contains the entry
point of the command interpreter
"""

import cmd
import sys
from os import isatty
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity

list_obj = ["BaseModel", "User", "Place", "City", "Review", "State", "Amenity"]
list_commands_arg = ["show()", "destroy()", "update()", "count()"]
list_commands_not_arg = ["create()", "all()"]
all_commands = list_commands_arg + list_commands_not_arg


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand inherits from cmd.Cmd to be our entry point
    """

    prompt = "(hbnb) "

    def default(self, line):
        """
        Method to advance task
        """
        if "." not in line:
            self.stdout.write(f'*** Unknown syntax: {line}\n')
            return False
        args = line.split(".")

        model = args[0] if len(args) > 0 else ""
        command = args[1] if len(args) > 1 else ""
        arguments = command.split(
            "(")[1][:-1].replace("\"", "").replace(",", "")

        if "(" in command and ")" in command:
            for word in command.split("("):
                word = word + "()"
                if word in all_commands:
                    command = word
                    break
        if model in list_obj and command in all_commands:
            if len(arguments) > 1 and command in list_commands_arg:
                command = command[:-2]
                eval(f"self.do_{command}('{model} {arguments}')")
            else:
                command = command[:-2]
                eval(f"self.do_{command}({model})")
        else:
            self.stdout.write(f'*** Unknown syntax: {line}\n')

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """

        try:
            arg = arg.__name__
        except Exception:
            pass

        if not arg:
            print("** class name missing **")
        elif arg not in list_obj:
            print("** class doesn't exist **")
        else:
            obj = eval(f"{arg}()")
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an
        instance based on the class name and id
        """

        try:
            arg = arg.__name__
        except Exception:
            pass
        list_arg = arg.split(" ")
        try:
            model = list_arg[0]
            id_recieved = list_arg[1]
        except Exception:
            pass

        if not arg:
            print("** class name missing **")
        elif model not in list_obj:
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        else:
            found_it = False
            all_objs = models.storage.all()
            for obj_id in all_objs.keys():
                if all_objs[obj_id].id == id_recieved:
                    found_it = True
                    obj = all_objs[obj_id]
                    print(obj)
            if found_it is False:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        try:
            arg = arg.__name__
        except Exception:
            pass

        all_objs = models.storage.all()
        obj_to_print = []

        if not arg:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                obj_to_print.append(obj.__str__())
            print(obj_to_print)
        elif arg in list_obj:
            for obj_id in all_objs.keys():
                if all_objs[obj_id].__class__.__name__ == arg:
                    obj = all_objs[obj_id]
                    obj_to_print.append(obj.__str__())
            print(obj_to_print)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        try:
            arg = arg.__name__
        except Exception:
            pass

        list_arg = arg.split(" ")

        try:
            model = list_arg[0]
            id_recieved = list_arg[1]
        except Exception:
            pass

        if not arg:
            print("** class name missing **")
        elif model not in list_obj:
            print("** class doesn't exist **")
        elif len(list_arg) < 2:
            print("** instance id missing **")
        else:
            found_it = False
            all_objs = models.storage.all()
            copy = all_objs.copy()
            for obj_id in copy.keys():
                if copy[obj_id].id == id_recieved:
                    found_it = True
                    all_objs.pop(obj_id)
            models.storage.save()
            if found_it is False:
                print("** no instance found **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """

        list_arg = arg.split(" ")
        if not list_arg[0]:
            print("** class name missing **")
            return False
        elif list_arg[0] not in list_obj:
            print("** class doesn't exist **")
            return False
        if len(list_arg) < 2:
            print("** instance id missing **")
            return False
        id_recieved = list_arg[1]
        found_it = False
        all_objs = models.storage.all()
        copy = all_objs.copy()
        for obj_id in copy.keys():
            if copy[obj_id].id == id_recieved:
                found_it = True
                if len(list_arg) < 3:
                    print("** attribute name missing **")
                    return False
                elif len(list_arg) < 4:
                    print("** value missing **")
                    return False

                attr_name = list_arg[2]
                attr_value = list_arg[3]

                if attr_value.startswith("\""):
                    attr_value = ' '.join([str(n) for n in list_arg[3:]])
                    if attr_value.startswith("\"")\
                            and attr_value.endswith("\""):
                        attr_value = attr_value[1:-1]
                else:
                    if "." in attr_value:
                        attr_value = float(attr_value)
                    elif attr_value.isdigit():
                        attr_value = int(attr_value)

                obj = all_objs[obj_id]
                setattr(obj, attr_name, attr_value)

        models.storage.save()
        if found_it is False:
            print("** no instance found **")

    def do_count(self, arg):
        """
        Method to count Models
        """
        try:
            arg = arg.__name__
        except Exception:
            pass

        all_objs = models.storage.all()
        count = 0

        if arg in list_obj:
            for obj_id in all_objs.keys():
                if all_objs[obj_id].__class__.__name__ == arg:
                    count = count + 1
            print(count)

    def do_quit(self, arg):
        """
        quit and EOF to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF to exit the program
        """
        return True

    def emptyline(self):
        """
        ENTER shouldn’t execute anything
        """
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()

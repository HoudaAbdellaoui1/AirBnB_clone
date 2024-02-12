#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the HBNB project.
    Attributes:
        prompt (str): The prompt displayed to the user."""

    prompt = '(hbnb) '

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, arg):
        """Creates a new instance and saves it to the JSON file."""
        try:
            class_name = self.parse_line(arg)
            if not class_name:
                return SyntaxError("** class name missing **")

            obj = eval("{}()".format(class_name))
            self.set_attributes(obj, arg)
            obj.save()
            print("{}".format(obj.id))

        except SyntaxError as se:
            print(se)
        except NameError:
            print("** class doesn't exist **")

    def set_attributes(self, obj, line):
        """Sets attributes of the object based on the input line."""
        args = line.split(" ")
        for arg in args[1:]:
            p_v = self.valid_param(arg)
            if p_v:
                setattr(obj, p_v[0], p_v[1])

    def valid_param(self, arg):
        """Validates parameter and returns either None or a tuple."""
        if "=" not in arg:
            return None

        param, value = arg.split("=")
        try:
            value = eval(value)
        except Exception:
            return None

        if isinstance(value, str):
            value = value.replace("_", " ")

        return param, value

    def do_show(self, line):
        """Prints the string representation of an instance
        Args:
            line (str): The arguments passed with the command.
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all(eval(my_list[0]))
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        try:
            if not arg:
                raise SyntaxError()
            my_list = arg.split(" ")
            if my_list[0] not in self.classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representations of instances.
        Args:
            arg (str): The arguments passed with the command."""
        args = line.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in storage.all(self
                                               .classes[args[0]]).values()])

    def parse_line(self, line):
        """Parses the line into class name."""
        if not line:
            return None

        class_name = line.strip()
        if class_name not in self.classes:
            raise NameError()

        return class_name

    def do_update(self, line):
        """Updates an instance by adding or updating attribute."""
        try:
            if not line:
                raise SyntaxError()
            my_list = split(line, " ")
            if my_list[0] not in self.classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def emptyline(self):
        """
        Do nothing on empty input.

        This prevents executing the last command when the user presses
        ENTER without typing anything.
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF (Ctrl+D) to exit the program"""
        print("")  # New line for better formatting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

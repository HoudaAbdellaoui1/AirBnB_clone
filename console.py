#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the HBNB project.
    Attributes:
        prompt (str): The prompt displayed to the user."""

    prompt = '(hbnb) '

    classes = {
        "BaseModel": BaseModel
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
        try:
            class_name = self.parse_line(line)
            objects = storage.all()

            if class_name:
                objects = {k: v for k, v in objects.items() if class_name in k}

            if not objects:
                print("**  no instance found **")
                return

            print([str(obj) for obj in objects.values()])

        except NameError:
            print("** class doesn't exist **")

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

    def parse_update_line(self, line):
        """Parses the line into class name, object ID, attribute, and value."""
        if not line:
            raise SyntaxError()

        args = line.split(" ")
        if len(args) < 4:
            raise SyntaxError()

        class_name, obj_id, attribute, value = args[0], args[1], args[2], args[3]

        if class_name not in self.classes:
            raise NameError("** class doesn't exist **")

        if not obj_id:
            raise IndexError("** instance id missing **")

        if not attribute:
            raise AttributeError("** attribute name missing **")

        if not value:
            raise ValueError("** value missing **")

        return class_name, obj_id, attribute, value

    def emptyline(self):
        """
        Do nothing on empty input.

        This prevents executing the last command when the user presses
        ENTER without typing anything.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

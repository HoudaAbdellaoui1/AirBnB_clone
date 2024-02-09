import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.

    Attributes:
        prompt (str): The prompt displayed to the user.
    """

    prompt = '(hbnb) '

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel and saves it to the JSON file.

        Args:
            arg (str): The argument passed with the command.

        Usage:
            create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.

        Args:
            arg (str): The arguments passed with the command.

        Usage:
            show <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
                return
        except IndexError:
            print("** class name missing **")
            return

        try:
            obj_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        key = class_name + "." + obj_id
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Args:
            arg (str): The arguments passed with the command.

        Usage:
            destroy <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
                return
        except IndexError:
            print("** class name missing **")
            return

        try:
            obj_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        key = class_name + "." + obj_id
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances.

        Args:
            arg (str): The arguments passed with the command.

        Usage:
            all [<class name>]
        """
        objects = storage.all()
        args = arg.split()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        try:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
                return
        except IndexError:
            print("** class name missing **")
            return

        print([str(obj) for key, obj in objects.items() if class_name in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.

        Args:
            arg (str): The arguments passed with the command.

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
                return
        except IndexError:
            print("** class name missing **")
            return

        try:
            obj_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return

        key = class_name + "." + obj_id
        if key not in storage.all():
            print("** no instance found **")
            return

        try:
            attribute_name = args[2]
        except IndexError:
            print("** attribute name missing **")
            return

        try:
            attribute_value = args[3]
        except IndexError:
            print("** value missing **")
            return

        obj = storage.all()[key]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass

        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def emptyline(self):
        """
        Do nothing on empty input.

        This prevents executing the last command when the user presses
        ENTER without typing anything.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

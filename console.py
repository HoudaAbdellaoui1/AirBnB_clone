import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.

    Attributes:
        prompt (str): The prompt displayed to the user.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): The argument passed with the command (ignored).

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF is reached (Ctrl+D).

        Args:
            arg (str): The argument passed with the command (ignored).

        Returns:
            bool: True to exit the program.
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing on empty input.

        This prevents executing the last command when the user presses
        ENTER without typing anything.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

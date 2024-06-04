#!/usr/bin/python3
"""
This defines the console class
which will be the entry point
for the cli
"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """
        Default behavior for cmd module
        when the input is wrong
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destory": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def do_create(self, arg):
        """
        Creates a new class instance
        """
        arg1 = parse(arg)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()
        
        def do_show(self, arg):
            """
            Display the string of a class instance
            """
            arg1 = parse(arg)
            objdict = storage.all()
            if len(arg1) == 0:
                print("** class name missing **")
            elif arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist")
            elif len(arg1) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(arg1[0], arg1[1]) not in objdict:
                print ("** no instance found **")
            else:
                print(objdict["{}.{}".format(arg1[0], arg1[1])])
        
        def do_destroy(self, arg):
            """
            Delete a class
            """
            arg1 = parse(arg)
            objdict = storage.all()
            if len(arg1) == 0:
                print("** class name missing **")
            elif arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist")
            elif len(arg1) == 1:
                print("** instance id missing")
            elif "{}.{}".format(arg1[0], arg1[1]) not in objdict.keys():
                print("** no instance found")
            else:
                del objdict["{}.{}".format(arg1[0], arg1[1])]
                storage.save()

        def do_all(self, arg):
            """
            Display all instances of a class
            """
            arg1 = parse(arg)
            if len(arg1) > 0 and arg1[0] not in HBNBCommand.__classes:
                print("** class doesn't exist")
            else:
                obj1 = []
                for obj in storage.all().values():
                    if len(arg1) > 0 and arg1[0] == obj.__class.__name__:
                        obj1.append(obj.__str__())
                    elif len(arg1) == 0:
                        obj1.append(obj.__str__())
                print(obj1)

    def do_update(self, arg):
        """
        Update a class instance
        """
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

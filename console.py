#!/usr/bin/env python3
"""
Console for object management and storage persistant
"""
import cmd
import json
import os
import sys
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

""" definition to implemente EOF, quit and emptyline commands"""   
    def do_EOF(self, args):
        """Handles End Of File character\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        exit(0)

    def emptyline(self):
        """ pass line """
        pass


    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        Syntax:
            create [name]
        Example:
            $ create BaseModel"""

        try:
            arguments = args.split()
        if args == "" or args is None:
            print("** class name missing **")
	    return		
        elif args not in storage.classes():
            print("** class doesn't exist **")
	    return

        obj = models.classes[args]()
        models.storage.save()
        self.__print(obj.id)   



    def do_show(self, args):
            """ Prints the string representation of an instance
            Syntax:
                    show [name] [id]
            Example:
                    $ show BaseModel 1234-1234-1234"""
            
            arguments = args.split()
	        if not args:
                print("** class name missing **")
                return
            elif arguments[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            elif len(arguments) == 1:
                print("** instance id missing **")
                return
             else:
                 key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        Syntax:
            destroy [name] [id]	TO DO
        Example:
            $ destroy BaseModel 1234-1234-1234"""



    def do_all(self, args):
        """Prints all string representation of all instances based
        or not on the class name
        Syntax:
            all [name]	TO DO
        Example:
            $ all BaseModel or $ all"""

    def do_update(self, args):
        """ Command that update a class.
        Syntax:
            update <class name> <id> <at name> "<at value>	TO DO
        Example:
            $ update User 1234-1234-1234 email "aibnb@hbtn.com
        """                       







if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" Defines a base model class """

class Base:
__nb_objects = 0


def __init__(self, id=None):
    """ Initialize a new Base """
    if id is not None
    self.id = id
else:
    Base__nb_objects += 1
    self.id = Base__nb_objects

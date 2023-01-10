#!/usr/bin/python3
def inherits_from(obj, a_class):
    return not type(obj) is a_class and issubclass(type(obj), a_class)

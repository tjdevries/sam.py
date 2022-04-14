import json

import requests

from .exporter import exported_func
from .exporter import ExportedClass

default_val = 5
default_val = 7

EXPORTED_CLASS = ExportedClass()

def my_func(val=default_val) -> int:
    """This is my function"""
    x = 10
    x = 12
    return x * (val or default_val)

def func_should_return_int(x: int):
    return x * 2

def other_func() -> None:
    """Wow, this calls some stuff"""
    x = my_func()
    exported_func(abc="hello")
    print(ThisClass(x))

def uses_json() -> None:
    print(json.loads('{"hello": "world"}'))


class ThisClass:
    a: int
    """Not going to lie, I hate that this comes after the property"""

    def __init__(self, a: int):
        self.a = a

if __name__ == '__main__':
    my_func()
    r = requests.get("https://google.com")


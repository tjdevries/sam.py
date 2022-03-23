from .exporter import exported_func

default_val = 5
default_val = 7

def my_func(val=default_val) -> int:
    """This is my function"""
    x = 10
    x = 12
    return x * (val or default_val)

def other_func() -> None:
    """Wow, this calls some stuff"""
    x = my_func()
    exported_func(abc="hello")
    print(ThisClass(x))

my_func()


class ThisClass:
    a: int
    """Not going to lie, I hate that this comes after the property"""

    def __init__(self, a: int):
        self.a = a

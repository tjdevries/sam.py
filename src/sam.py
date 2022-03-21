from .exporter import exported_func

def my_func() -> int:
    """This is my function"""
    return 5

def other_func() -> None:
    """Wow, this calls some stuff"""
    x = my_func()
    exported_func(a="hello")
    print(ThisClass(x))

my_func()


class ThisClass:
    a: int
    """Not going to lie, I hate that this comes after the property"""

    def __init__(self, a: int):
        self.a = a

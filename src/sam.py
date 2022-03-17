from .exporter import exported_func

def my_func() -> int:
    """This is my function"""
    return 5

def other_func() -> None:
    """Wow, this calls some stuff"""
    x = my_func()
    exported_func("hello",  "world")
    print(x)

my_func()

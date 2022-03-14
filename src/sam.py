from .exporter import exported_func

def my_func() -> None:
    """This is my function"""
    pass

def other_func() -> None:
    """Wow, this calls some stuff"""
    my_func()
    exported_func()

if __name__ == "__main__":
    my_func()

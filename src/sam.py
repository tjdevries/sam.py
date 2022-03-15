from .exporter import exported_func

def my_func() -> int:
    """This is my function"""
    return 5

def other_func() -> None:
    """Wow, this calls some stuff"""
    x = my_func()
    exported_func()
    print(x)

if __name__ == "__main__":
    my_func()

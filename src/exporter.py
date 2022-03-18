def my_decorator(f):
    return f


@my_decorator
def exported_func(a: str, b: str = ", World!") -> str:
    """This is the
    docstring from
    an exported function"""
    return a + b

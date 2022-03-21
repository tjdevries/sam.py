def my_decorator(f):
    return f


@my_decorator
def exported_func(abc: str, b: str = ", World!") -> str:
    """This is the
    docstring from
    an exported function

    :param abc: Describing cool parameter `abc`
    """
    return abc + b

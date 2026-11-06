def build_instances(cls, count: int) -> list:
    """
    Return a list of `count` NEW instances of the class `cls`,
    each created by calling `cls()` with no arguments. Every
    instance must be a separate object. If count <= 0, return [].
    """
    if count <= 0:
        return []
    return [cls() for _ in range(count)]


def attach_point(obj, x: int, y: int) -> None:
    """
    Set two attributes on `obj`: obj.x = x and obj.y = y. If the
    attributes already exist, replace their values. Return
    nothing.
    """
    obj.x = x
    obj.y = y


def same_class(a, b) -> bool:
    """
    Return True if `a` and `b` are instances of exactly the same
    class (compare type(a) and type(b) with `is`).
    """
    return type(a) is type(b)


def attribute_snapshot(obj) -> dict:
    """
    Return a NEW dictionary containing a copy of the attributes
    stored on `obj` (from obj.__dict__). Changing the returned
    dictionary must not change `obj`.
    """
    return dict(obj.__dict__)


class Rectangle:
    """
    A rectangle with a width and a height.

    __init__(self, width, height):
        Store the two arguments as instance attributes `width`
        and `height`.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height


class Account:
    """
    A simple account record.

    __init__(self, owner, balance=0, history=None):
        Store `owner` and `balance` as attributes.
        Store `history` as an attribute holding a list of past
        transaction amounts. If `history` is None, use a NEW
        empty list for THIS instance. If a list is given, store
        an independent copy of it (list(history)), so the
        instance does not share the caller's list.
    """

    def __init__(self, owner, balance=0, history=None):
        self.owner = owner
        self.balance = balance
        if history is None:
            history = []
        self.history = list(history)


def make_rectangle(width, height):
    """
    Return a new Rectangle with the given width and height.
    """
    return Rectangle(width, height)


def attributes_of(obj) -> dict:
    """
    Return a NEW dictionary that is a copy of obj.__dict__.
    """
    return dict(obj.__dict__)

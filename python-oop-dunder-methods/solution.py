class Vec:
    """
    A fixed sequence of numbers.

    __init__(self, *components):
        Store the components in an attribute `data`, as a list.

    __repr__(self):
        Return a string of the form "Vec(1, 2, 3)" showing the
        components separated by ", ". An empty Vec is "Vec()".

    __eq__(self, other):
        If `other` is not a Vec, return NotImplemented. Otherwise
        return True if both have the same components in the same
        order, False otherwise.

    __len__(self):
        Return the number of components.

    __getitem__(self, index):
        If `index` is an int, return that component (negative
        indices allowed, out-of-range raises IndexError as a list
        does). If `index` is a slice, return a NEW Vec holding
        the selected components.
    """

    def __init__(self, *components):
        self.data = list(components)

    def __repr__(self):
        return f"Vec({', '.join(repr(c) for c in self.data)})"

    def __eq__(self, other):
        if not isinstance(other, Vec):
            return NotImplemented
        return self.data == other.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return Vec(*self.data[index])
        return self.data[index]

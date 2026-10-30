def index_or_minus_one(lst: list, value) -> int:
    """
    Return the index of the first element of `lst` that matches
    `value`, or -1 if there is none. Do not let index() raise.
    """
    try:
        return lst.index(value)
    except ValueError:
        return -1

def all_indices(lst: list, value) -> list:
    """
    Return a list of every index at which `lst` holds an element
    equal to `value`, in increasing order. Use enumerate().

    Example: all_indices([5, 3, 5, 7], 5) -> [0, 2]
    """
    return [i for i, x in enumerate(lst) if x == value]


def contains_all(lst: list, needles: list) -> bool:
    """
    Return True if every element of `needles` is present in
    `lst`. An empty `needles` returns True.
    """
    return all(needle in lst for needle in needles)


def contains_same_object(lst: list, target) -> bool:
    """
    Return True if some element of `lst` IS the exact object
    `target` (identity, using `is`), even if equal-looking
    objects elsewhere in the list do not count.

    Example: a = [1]; contains_same_object([[1], a], a) -> True
             contains_same_object([[1]], a)             -> False
    """
    return any(x is target for x in lst)


def sorted_desc_copy(lst: list) -> list:
    """
    Return a NEW list containing the elements of `lst` sorted in
    descending order. `lst` itself must not change.
    """
    return sorted(lst, reverse=True)


def sort_in_place_by_length(words: list) -> None:
    """
    Sort `words` in place by the length of each string, shortest
    first. Words of equal length must keep their original
    relative order. Use sort() with key=len. Return nothing.
    """
    words.sort(key=len)


def last_char(word: str) -> str:
    """
    Return the last character of `word`, or "" if `word` is
    empty. (Used as a sort key below.)
    """
    if word == "":
        return ""
    return word[-1]
    

def sort_by_last_char(words: list) -> list:
    """
    Return a NEW list of the elements of `words`, sorted by
    their last character (using last_char as the key). Ties
    keep their original order. `words` itself must not change.
    """
    return sorted(words, key=last_char)


def reversed_copy(lst: list) -> list:
    """
    Return a NEW list with the elements of `lst` in reverse
    order. Use reversed() and list(). `lst` must not change.
    """
    return list(reversed(lst))

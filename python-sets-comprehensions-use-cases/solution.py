def squared_unique(values) -> set:
    """
    Return a set containing the square of every value in `values`.

    Duplicate square results must appear only once.

    Example:
        squared_unique([-2, -1, 1, 2]) -> {1, 4}
    """
    return {x * x for x in values}


def positive_unique(values) -> set:
    """
    Return a set containing every distinct positive value from
    `values`.

    Zero and negative values must not appear.

    Example:
        positive_unique([-2, 3, 3, 0, 5, -1]) -> {3, 5}
    """
    return {x for x in values if x > 0}


def word_lengths(words: list) -> set:
    """
    Return a set containing the lengths of all words in `words`.

    Example:
        word_lengths(["cat", "dog", "house"]) -> {3, 5}
    """
    return {len(word) for word in words}


def coordinate_sums(points: list) -> set:
    """
    `points` is a list of 2-element tuples `(x, y)`.

    Return a set containing `x + y` for every point.

    Example:
        coordinate_sums([(1, 2), (3, 4), (0, 3)]) -> {3, 7}
    """
    return {x + y for x, y in points}


def find_duplicates(values: list) -> set:
    """
    Return a set containing every value that appears more than
    once in `values`.

    Each duplicated value must appear only once in the result.

    Example:
        find_duplicates([1, 2, 1, 3, 2, 2]) -> {1, 2}

    Do not modify `values`.
    """
    seen = set()
    duplicates = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)
    return duplicates


def unique_in_first_seen_order(values: list) -> list:
    """
    Return a new list containing each distinct value from `values`
    exactly once, in the order in which each value first appeared.

    Use a set to track which values have already been seen and a
    list to preserve the required output order.

    Example:
        unique_in_first_seen_order([3, 1, 3, 2, 1]) -> [3, 1, 2]
    """
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def all_seen_before(values: list) -> bool:
    """
    Return True if every element after the first occurrence of a
    value is a repeated occurrence of a value already seen.

    More directly: return True when the sequence contains no value
    that appears exactly once, and False otherwise.

    Example:
        all_seen_before([1, 2, 1, 2]) -> True
        all_seen_before([1, 2, 1]) -> False
    """
    counts = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return all(count != 1 for count in counts.values())


def missing_values(values: list, expected: set) -> set:
    """
    Return the elements from `expected` that never occur in
    `values`.

    Example:
        missing_values([1, 3, 3], {1, 2, 3, 4}) -> {2, 4}

    Do not modify either input.
    """
    return expected - set(values)

def word_frequencies(text: str) -> dict:
    """
    Split `text` on whitespace and return a dictionary mapping
    each word to the number of times it occurs. Case matters:
    "The" and "the" are different words. Use get() with a
    default of 0.

    Example: word_frequencies("a b a") -> {"a": 2, "b": 1}
    """
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def safe_lookup(d: dict, key, default):
    """
    Return the value stored under `key` in `d`, or `default` if
    `key` is not present. Do not modify `d`. Use get().
    """
    return d.get(key, default)


def increment(d: dict, key, amount: int) -> None:
    """
    Add `amount` to the number stored under `key` in `d`, in
    place. If `key` is not present, store `amount` under it.
    Return nothing.
    """
    d[key] = d.get(key, 0) + amount


def dict_from_two_lists(keys: list, values: list) -> dict:
    """
    `keys` and `values` are lists of the same length. Return a
    new dictionary that maps keys[i] to values[i] for every
    position i. Use an index loop (range and len). If a key
    repeats, the LAST value wins.

    Example: dict_from_two_lists(["a", "b"], [1, 2]) -> {"a": 1, "b": 2}
    """
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result


def merge_prefer_second(a: dict, b: dict) -> dict:
    """
    Return a NEW dictionary containing every entry of `a` and
    every entry of `b`. If a key is in both, the value from `b`
    is used. Neither `a` nor `b` may be modified. Build the
    result by copying `a` with dict(a) and then calling update().
    """
    result = dict(a)
    result.update(b)
    return result


def merge_counts(a: dict, b: dict) -> dict:
    """
    `a` and `b` map keys to integer counts. Return a NEW
    dictionary in which each key's value is the sum of its
    values in `a` and `b` (a missing key counts as 0). Neither
    input may be modified.

    Example: merge_counts({"x": 1, "y": 2}, {"y": 3, "z": 4})
             -> {"x": 1, "y": 5, "z": 4}
    """
    result = dict(a)
    for key, value in b.items():
        result[key] = result.get(key, 0) + value
    return result
    

def group_by_first_letter(words: list) -> dict:
    """
    Return a dictionary that maps each first letter (lowercase)
    to a list of the words that start with it, in input order.
    Use setdefault() to create each list. Ignore empty strings.
    Matching is case-insensitive for the key, but the words are
    stored as given.

    Example: group_by_first_letter(["Apple", "avocado", "Bean"])
             -> {"a": ["Apple", "avocado"], "b": ["Bean"]}
    """
    result = {}
    for word in words:
        if not word:
            continue
        letter = word[0].lower()
        result.setdefault(letter, []).append(word)
    return result


def add_defaults(config: dict, defaults: dict) -> None:
    """
    Add to `config`, in place, every entry of `defaults` whose
    key is not already in `config`. Existing keys keep their
    values. Use setdefault(). Return nothing.
    """
    for key, value in defaults.items():
        config.setdefault(key, value)


def remove_keys(d: dict, keys: list) -> int:
    """
    Remove from `d`, in place, every key listed in `keys` that is
    present in `d`. Keys not present are ignored. `keys` may
    contain duplicates. Return the number of entries actually
    removed.

    Example: d = {"a": 1, "b": 2}; remove_keys(d, ["a", "z", "a"])
             -> returns 1, and d is now {"b": 2}
    """
    removed = 0 
    for key in keys:
        if key in d:
            del d[key]
            removed += 1
    return removed


def take_last(d: dict):
    """
    Remove the most recently inserted entry from `d`, in place,
    and return it as a (key, value) tuple. If `d` is empty,
    return None and leave `d` unchanged. Use popitem().
    """
    if not d:
        return None
    return d.popitem()


def remove_and_return(d: dict, key, default):
    """
    Remove `key` from `d` in place and return its value. If the
    key is not present, return `default` and leave `d`
    unchanged. Use pop() with a default.
    """
    return d.pop(key, default)


def clear_and_report(d: dict) -> int:
    """
    Remove every entry from `d` in place and return how many
    entries there were before clearing.
    """
    count = len(d)
    d.clear()
    return count

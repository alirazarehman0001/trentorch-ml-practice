def sentence_case(s: str) -> str:
    """
    Return `s` with its first character uppercase and every
    other character lowercase.
    Example: sentence_case("hELLO wORLD") -> "Hello world"
    """
    return s.capitalize()


def swap_first_char_case(s: str) -> str:
    """
    Return `s` with ONLY its first character's case swapped;
    the rest of the string is unchanged. An empty string
    returns "". Use slicing together with swapcase().
    Example: swap_first_char_case("python") -> "Python"
             swap_first_char_case("PYthon") -> "pYthon"
    """
    if len(s) == 0:
        return s
    return s[0].swapcase() + s[1:]


def equal_ignoring_case(a: str, b: str) -> bool:
    """
    Return True if `a` and `b` are the same text when case is
    ignored. Use casefold() on both sides.
    Example: equal_ignoring_case("Straße", "STRASSE") -> True
    """
    return a.casefold() == b.casefold()
        


def case_kind(s: str) -> str:
    """
    Classify `s` using isupper(), islower(), and istitle(),
    checked in this order. Return exactly one of:
      "upper", "lower", "title", "mixed"
    Return "mixed" if none of the three tests is True
    (including for the empty string).
    """
    if s.isupper():
        return "upper"
    elif s.islower():
        return "lower"
    elif s.istitle():
        return "title"
    else:
        return "mixed"


def find_all(s: str, sub: str):
    """
    Return a list of the starting indices of every occurrence
    of `sub` in `s`, in increasing order, INCLUDING overlapping
    occurrences. Use find() with a moving start position.
    If `sub` is empty, return an empty list.

    Example: find_all("aaaa", "aa") -> [0, 1, 2]
    """
    result = []
    start = 0
    if len(sub) == 0:
        return result
    while True:
        find = s.find(sub, start)
        if find == -1:
            break
        result.append(find)
        start = find + 1
    return result

def count_overlapping(s: str, sub: str) -> int:
    """
    Return the number of occurrences of `sub` in `s`, counting
    overlapping occurrences. If `sub` is empty, return 0.
    Example: count_overlapping("aaaa", "aa") -> 3
             (the built-in count() would give 2)
    """
    return len(find_all(s, sub))


def has_extension(filename: str, ext: str) -> bool:
    """
    Return True if `filename` ends with a dot followed by `ext`,
    ignoring case. `ext` is given WITHOUT the dot.
    Example: has_extension("Report.PDF", "pdf") -> True
             has_extension("pdf", "pdf")        -> False
    """
    return filename.lower().endswith("." + ext.lower()) 


def classify_token(token: str) -> str:
    """
    Return exactly one of the following, checked in this order:
      "digits"  if every character is a digit
      "letters" if every character is a letter
      "alnum"   if every character is a letter or digit
      "space"   if every character is whitespace
      "other"   otherwise (including the empty string)
    """
    if token.isdigit():
        return "digits"
    elif token.isalpha():
        return "letters"
    elif token.isalnum():
        return "alnum"
    elif token.isspace():
        return "space"
    else:
        return "other"


def clean_field(s: str) -> str:
    """
    Return `s` with, in this order:
      1. leading and trailing whitespace removed,
      2. any trailing characters from the set ".,;" removed,
      3. leading and trailing whitespace removed again.

    Example: clean_field("  total ; ")  -> "total"
             clean_field("  a b.. ")    -> "a b"
    """
    s = s.strip()
    s = s.rstrip(".,;")
    s = s.strip()
    return s


def remove_prefix_once(s: str, prefix: str) -> str:
    """
    If `s` begins with `prefix`, return `s` with that prefix
    removed exactly ONCE. Otherwise return `s` unchanged.
    Do not use lstrip(): it removes a set of characters, not a
    prefix.

    Example: remove_prefix_once("ababab", "ab") -> "abab"
    """
    if prefix and s.startswith(prefix):
        return s[len(prefix):]
    return s


def replace_first_n(s: str, old: str, new: str, n: int) -> str:
    """
    Return `s` with the first `n` occurrences of `old` replaced
    by `new`. If n == 0, return `s` unchanged. If n < 0,
    replace every occurrence.
    """
    if n == 0:
        return s
    elif n < 0:
        return s.replace(old, new)
    else:
        return s.replace(old, new, n)

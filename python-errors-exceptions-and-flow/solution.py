def validate_age(age: int) -> int:
    """
    Return `age` if it is an int from 0 to 150 inclusive.
    Otherwise raise a ValueError whose message is exactly
      "age must be between 0 and 150"
    """
    if not 0 <= age <= 150:
        raise ValueError("age must be between 0 and 150")
    return age
    

def level_three(log: list) -> None:
    """
    Do these steps, in order:
      1. Append the string "L3 start" to `log`.
      2. Raise a RuntimeError with the message "boom".
      3. Append the string "L3 end" to `log`.
    (Step 3 must be written, and it must never run.)
    """
    log.append("L3 start")
    raise RuntimeError("boom")
    log.append("L3 end")


def level_two(log: list) -> None:
    """
    Append "L2 start" to `log`, call level_three(log), then
    append "L2 end" to `log`.
    """
    log.append("L2 start")
    level_three(log)
    log.append("L2 end")


def level_one(log: list) -> None:
    """
    Append "L1 start" to `log`, call level_two(log), then
    append "L1 end" to `log`.
    """
    log.append("L1 start")
    level_two(log)
    log.append("L1 end")


def first_element(items: list):
    """
    Return the first element of `items` by indexing position 0.
    Do not check for an empty list: an empty list should make
    Python itself raise an IndexError.
    """
    return items[0]

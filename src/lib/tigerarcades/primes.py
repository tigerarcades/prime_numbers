def is_prime_number(value: int) -> bool:
    """
    Tests if the given number is a prime number or not.

    Args:
        value: An integer value.
    Returns:
        True, if the value is a prime number, False else.
    """
    if value <= 3:
        return value > 1
    if value % 2 == 0 or value % 3 == 0:
        return False
    counter = 5
    while counter ** 2 <= value:
        if value % counter == 0 or value % (counter + 2) == 0:
            return False
        counter += 6
    return True

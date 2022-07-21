"""Logic module for brain-progression game."""


def ar_progression(start, step, iterations):
    """Create an arithmetic progression.

    Args:
        start: first number of progression
        step: difference between elements
        iterations: amount of elements

    Returns:
        return: arithmetic progression
    """
    first_num = start
    final = ''
    for num in range(1, iterations + 1):
        final += (str(first_num) + ' ')
        first_num += step
    return final.split()

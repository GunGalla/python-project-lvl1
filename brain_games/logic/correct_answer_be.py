"""Logic module for Brain-games."""


def correct_answer(num):
    """Define correct answer.

    Args:
        num: a number which askes is even or not

    Returns:
        return: variable with correct answer
    """
    if (num % 2 == 0) is True:
        ans = 'yes'
    else:
        ans = 'no'
    return ans

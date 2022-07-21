"""Logic module for Brain-games."""


def correct_answer(num):
    """Define correct answer.

    Args:
        num: a number which askes is even or not

    Returns:
        return: variable with correct answer
    """
    divider = 2
    while divider ** 2 <= num and num % divider != 0:
        divider += 1
    if (divider ** 2 > num) is True:
        ans = 'yes'
    else:
        ans = 'no'
    return ans

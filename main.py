def happy_num(num):
    """
    A happy numbers is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the
    squares of its digits, and repeat the process until the number equals
    1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

    :param n: Input number
    :return: True if n is a happy number, False otherwise

    Examples:

    >>> is_happy(19)
    True

    >>> is_happy(2)
    False

    >>> is_happy(44)
    True
    """
    
    seen = set()
    while (num != 1) and (num not in seen):
        seen.add(num)
        l = sum([int(x)**2 for x in str(num)])
    return l == 1

if __name__ == "__main__":
    assert happy_num(4) is False
    assert happy_num(100) is True

#input num
#sum
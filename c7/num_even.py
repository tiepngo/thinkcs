import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(num_even_digits(123456) == 3)
    test(num_even_digits(2468) == 4)
    test(num_even_digits(1357) == 0)
    test(num_even_digits(0) == 1)
    test(num_even_digits(20) == 2)

def num_even_digits(n):
    """Count the number of even digit in n"""
    sum = 0
    if n == 0 :
        return 1
    while n > 0 :
        temp = n % 10
        if temp % 2 == 0:
            sum += 1
        n //= 10
    return sum

test_suite()
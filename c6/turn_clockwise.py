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
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) is None)
    test(turn_clockwise("rubbish") is None)
    test(turn_clockwise("N") == "W")


def turn_clockwise(compass):
    if compass == "N":
        return "W"
    elif compass == "W":
        return "N"
    elif compass == "E":
        return "S"
    elif compass == "S":
        return "E"
    return None


test_suite()  # Here is the call to run the tests

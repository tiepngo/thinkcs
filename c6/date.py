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
    test(day_name(3) == "Wed")
    test(day_name(6) == "Sat")
    test(day_name(42) is None)
    test(day_num("Fri") == 5)
    test(day_num("Sun") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thu")) == "Thu")
    test(day_num("Halloween") is None)


date_list = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


def day_num(date_name):
    if date_name in date_list:
        return date_list.index(date_name)
    else:
        return None


def day_name(date_num):
    if date_num in range(7):
        return date_list[date_num]
    else:
        return None


test_suite()

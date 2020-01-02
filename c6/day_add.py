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
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

date_list = ["Sunday", "Monday", "Tuesday", "Wedneday", "Thurday", "Friday", "Saturday"]


def day_name(date_num):
    if date_num in range(7):
        return date_list[date_num]
    else:
        return None


def day_num(date_name):
    if date_name in date_list:
        return date_list.index(date_name)
    else:
        return None


def day_add(date_name, delta):
    current_date = day_num(date_name) + delta
    print("Debugging  current day , result ", current_date, current_date %7)
    return day_name(current_date % 7)

test_suite()
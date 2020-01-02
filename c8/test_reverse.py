def reverse(s):
    temp = s[::-1]
    return temp

def test_reverse():
    assert reverse("happy") == "yppah"
    assert reverse("Python") == "nohtyP"
    assert reverse("") == ""
    assert reverse("a") == "a"
    assert reverse("nobody") == "aaa"
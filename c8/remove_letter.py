def remove_letter(c,s):
    """Remove letter c from string s"""
    return s.replace(c,"")
    

def test_remove_letter():
    assert remove_letter("a", "apple") == "pple"
    assert remove_letter("a", "banana") == "bnn"
    assert remove_letter("z", "banana") == "banana"
    assert remove_letter("i", "Mississippi") == "Msssspp"
    assert remove_letter("b", "") == ""
    assert remove_letter("b", "c") == "c"
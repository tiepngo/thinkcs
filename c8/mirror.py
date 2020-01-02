def mirror(s):
    """Mirror string s"""
    return s + s[::-1]
    
def test_mirror():
    assert mirror("good") == "gooddoog"
    assert mirror("Python") == "PythonnohtyP"
    assert mirror("") == ""
    assert mirror("a") == "aa"
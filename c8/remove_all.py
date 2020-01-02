def remove_all(sub_s, s):
    """Remove all substring sub_s from string s"""
    return s.replace(sub_s,"")

def test_remove_all():
    assert remove_all("an", "banana") == "ba"
    assert remove_all("cyc", "bicycle") == "bile"
    assert remove_all("iss", "Mississippi") == "Mippi"
    assert remove_all("eggs", "bicycle") == "bicycle"
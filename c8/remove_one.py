def remove_one(sub_s,s):
    """Remove sub_string sub_s from string s for 1st occurence"""
    return s.replace(sub_s,"",1)

def test_remove_one():
    assert remove_one("an", "banana") == "bana"
    assert remove_one("cyc", "bicycle") == "bile"
    assert remove_one("iss", "Mississippi") == "Missippi"
    assert remove_one("eggs", "bicycle") == "bicycle"
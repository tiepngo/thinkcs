def count(sub_string,s):
    """Count substring sub_string in string s"""
    sum = 0
    i = s.find(sub_string,0)
    while i >=0 :
        sum += 1
        i = s.find(sub_string, i+1)
    return sum

def test_count_substring():
    assert count("is", "Mississippi") == 2
    assert count("an", "banana") == 2
    assert count("ana", "banana") == 2
    assert count("nana", "banana") == 1
    assert count("nanan", "banana") == 0
    assert count("aaa", "aaaaaa") == 4
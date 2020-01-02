def reverse(s):
    temp = s[::-1]
    return temp

def is_palindrome(s):
    """Check if a string s is palindrome
       a palindrome is a string s=reverse(s)"""
    return s == reverse(s)

def test_is_palindrome():
    assert is_palindrome("abba")
    assert not is_palindrome("abab")
    assert is_palindrome("tenet")
    assert not is_palindrome("banana")
    assert is_palindrome("straw warts")
    assert is_palindrome("a")
    assert is_palindrome("")    # Is an empty string a palindrome?
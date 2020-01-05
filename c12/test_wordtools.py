from wordtools import cleanword
from wordtools import has_dashdash
from wordtools import wordcount
from wordtools import wordset
from wordtools import longestword

def test_cleanword():
    assert cleanword("what?") == "what"
    assert cleanword("'now!'") == "now"
    assert cleanword("?+='w-o-r-d!,@$()'") == "word"

def test_has_dashdash():
    assert has_dashdash("distance--but")
    assert not has_dashdash("several")
    assert has_dashdash("spoke--")
    assert has_dashdash("distance--but")
    assert not has_dashdash("-yo-yo-")

def test_wordcount():
    assert wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2
    assert wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3
    assert wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1
    assert wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0

def test_wordset():
    assert wordset(["now", "is", "time", "is", "now", "is", "is"]) == ["is", "now", "time"]
    assert wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"]
    assert wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) == ["a", "am", "are", "be", "but", "is", "or"]

def test_longestword():
    assert longestword(["a", "apple", "pear", "grape"]) == 5
    assert longestword(["a", "am", "I", "be"]) == 2
    assert longestword(["this", "supercalifragilisticexpialidocious"]) == 34
    assert longestword([]) == 0
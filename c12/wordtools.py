from string import punctuation
import copy
def cleanword(s):
    """remove special character in string s"""
    word = ""
    for c in s:
        if c not in punctuation:
            word += c
    return word

def has_dashdash(s):
    """check if dash_dash -- is in string s"""
    return "--" in s

def wordcount(s,s_list):
    """Count string s in list of string"""
    return s_list.count(s)

def wordset(s_list):
    """Return unique element of string_list s_list"""
    s_set = set(s_list)
    s_list_sort = list(s_set)
    s_list_sort.sort()
    return s_list_sort

def longestword(s_list):
    """Return len of longest word in string list"""
    if len(s_list) == 0 :
        return 0
    return max([len(s) for s in s_list])
def count_letter_traversing(s,c) :
    """Count letter c in string s"""
    count = 0
    for i in s:
        if i == c:
            count += 1
    return count


def print_count_letter(s,c):
    """Caller of count_letter"""
    print(count_letter(s,c))

print_count_letter("banana","a")
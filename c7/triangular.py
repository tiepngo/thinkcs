def print_triangular_number(n):
    """print n first triangular number"""
    for i in range(1, n + 1):
        print(i, triangular_number(i))


def triangular_number(n):
    return n * (n + 1) / 2


print_triangular_number(5)

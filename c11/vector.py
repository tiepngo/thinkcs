"""This example cover exercise 11. --> 11."""
import pytest


def add_vectors(u, v):
    """Add 2 vector with same len"""
    if len(u) != len(v):
        print("Two vector must be same length")
        return -1
    else:
        temp = u[:]
        for i in range(len(temp)):
            temp[i] = u[i] + v[i]
        return temp


@pytest.mark.parametrize("x,y,expect", [([1, 1], [1, 1], [2, 2])])
def test_add_vector(x, y, expect):
    assert add_vectors(x, y) == expect

"""
    11.6 Write a function scalar_mult(s, v) that takes a number, s, and a list, v
    and returns the scalar multiple of v by s.
"""
def scalar_mult(s, v):
    """Multiple scalar s with vector v"""
    scalar = v[:]
    for i in range(len(v)):
        scalar[i] = s * v[i]
    return scalar

def test_scalar_mult():
    assert scalar_mult(5, [1, 2]) == [5, 10]
    assert scalar_mult(3, [1, 0, -1]) == [3, 0, -3]
    assert scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14]

"""
    11.7 Write a function dot_product(u, v) that takes two lists of numbers of the same length,
    and returns the sum of the products of the corresponding elements of each (the dot_product).
"""
def dot_product(u,v):
    """Dot product 2 vector with same len"""
    if len(u) != len(v):
        print("Two vector must be same length")
        return -1
    else:
        dot = 0
        for i in range(len(u)):
            dot += u[i] * v[i]
        return dot

def  test_dot_product():
    assert dot_product([1, 1], [1, 1]) == 2
    assert dot_product([1, 2], [1, 4]) == 9
    assert dot_product([1, 2, 1], [1, 4, 3]) == 12
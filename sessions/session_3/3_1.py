import string
import itertools
import functools


def test_1_1(*strings):
    """This function returns characters that appear in all strings"""
    return functools.reduce(set.intersection, map(set, strings))


def test_1_2(*strings):
    """This function returns characters that appear in at least one string"""
    return functools.reduce(set.union, map(set, strings))


def test_1_3(*strings):
    """This function returns characters that appear at least in two strings"""
    pairs = itertools.combinations(map(set, strings), 2)
    return functools.reduce(set.union, map(lambda p: p[0] & p[1], pairs))


def test_1_4(*strings):
    """This function returns characters of alphabet, that were not used in any string"""
    return set(string.ascii_lowercase) - test_1_2(*strings)


if __name__ == '__main__':
    test_strings = ["hello", "world", "python"]

    assert test_1_1(*test_strings) == {'o'}, 'Test 1 failed'
    assert test_1_2(*test_strings) == {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}, 'Test 2 failed'
    assert test_1_3(*test_strings) == {'h', 'l', 'o'}, 'Test 3 failed'
    assert test_1_4(*test_strings) == {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'},\
        'Test 4 failed'

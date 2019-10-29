import functools
import operator
import collections


def combine_dicts(*args):
    return functools.reduce(operator.add, map(collections.Counter, args))


if __name__ == '__main__':
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    assert combine_dicts(dict_1, dict_2) == {'a': 300, 'b': 200, 'c': 300}, 'Test 1 failed'
    assert combine_dicts(dict_1, dict_2, dict_3) == {'a': 600, 'b': 200, 'c': 300, 'd': 100}, \
        'Test 2 failed'

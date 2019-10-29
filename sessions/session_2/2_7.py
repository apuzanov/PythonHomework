import functools
import operator


def foo(input_list):
    total = functools.reduce(operator.mul, input_list)
    return [total/n for n in input_list]


if __name__ == '__main__':
    assert foo([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24], 'Test 1 failed!'
    assert foo([3, 2, 1]) == [2, 3, 6], 'Test 2 failed!'

def get_pairs(input_list):
    pairs = list(zip(input_list, input_list[1:]))
    return None if pairs == [] else pairs


if __name__ == '__main__':
    assert get_pairs([1, 2, 3, 8, 9]) == [(1, 2), (2, 3), (3, 8), (8, 9)], 'Test 1 failed'
    assert get_pairs(['need', 'to', 'sleep', 'more']) == [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]
    assert get_pairs([1]) is None, 'Test 3 failed'

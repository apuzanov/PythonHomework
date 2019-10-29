from itertools import zip_longest


def split_by_indexes(input_string, indexes):
    return [input_string[i:j] for i, j in zip_longest([None] + indexes, indexes) if input_string[i:j]]


if __name__ == '__main__':
    assert split_by_indexes("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == ["python", "is", "cool", ",", "isn't", "it?"], \
        'Test 1 failed!'
    assert split_by_indexes("no luck", [42]) == ["no luck"], 'Test 2 failed!'

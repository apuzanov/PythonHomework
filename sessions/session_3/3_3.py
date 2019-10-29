def count_letters(thestring):
    return {s: thestring.count(s) for s in thestring}


if __name__ == '__main__':
    assert count_letters("stringsample") == {'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1, 'a': 1, 'm': 1, 'p': 1,
                                             'l': 1, 'e': 1}, 'Test 1 failed'


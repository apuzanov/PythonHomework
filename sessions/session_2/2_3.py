import re


def split_str(string, sep=None, maxsplit=-1):
    string = string.strip()
    sep = sep or r'\W+'
    i = 0
    result = []

    if maxsplit != 0:
        split_count = 0
        for w in re.finditer(sep, string):
            result.append(string[i:w.start()])
            i = w.end()
            split_count += 1
            if maxsplit != -1 and maxsplit <= split_count:
                break

    if i <= len(string):
        result.append(string[i:])

    return result


if __name__ == '__main__':
    assert str.split('abcabcde') == split_str('abcabcde'), 'Test 1.1 failed'
    assert str.split('ab ca bc') == split_str('ab ca bc'), 'Test 1.2 failed'
    assert str.split('ab   ca   bc') == split_str('ab   ca   bc'), 'Test 1.3 failed'
    assert str.split('  ab   ca   bc') == split_str('  ab   ca   bc'), 'Test 1.4 failed'
    assert str.split('ab\nca\tbc') == split_str('ab\nca\tbc'), 'Test 1.5 failed'

    assert str.split('abcabca', 'b') == split_str('abcabca', 'b'), 'Test 2.1 failed'
    assert str.split('abcabc', 'bc') == split_str('abcabc', 'bc'), 'Test 2.2 failed'
    assert str.split('babbabb', 'b') == split_str('babbabb', 'b'), 'Test 2.3 failed'

    assert str.split('abcabc', 'b', maxsplit=0) == split_str('abcabc', 'b', maxsplit=0), 'Test 3.1 failed'
    assert str.split('abcabc', 'b', maxsplit=1) == split_str('abcabc', 'b', maxsplit=1), 'Test 3.2 failed'
    assert str.split('abcabc', 'b', maxsplit=2) == split_str('abcabc', 'b', maxsplit=2), 'Test 3.3 failed'

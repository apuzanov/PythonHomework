def get_longest_word(input_string: str) -> str:
    return sorted(input_string.split(), key=len, reverse=True)[0]


if __name__ == '__main__':
    assert get_longest_word("Python is simple and effective!") == 'effective!', 'Test 1 failed!'
    assert get_longest_word("Any pythonista like namespaces a lot.") == 'pythonista', 'Test 2 failed!'

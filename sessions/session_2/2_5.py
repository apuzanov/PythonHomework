def get_digits(num):
    return tuple(map(int, str(num)))


if __name__ == '__main__':
    assert get_digits(123) == (1, 2, 3), 'Test 1 failed!'
    assert get_digits(87178291199) == (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9), 'Test 2 failed!'

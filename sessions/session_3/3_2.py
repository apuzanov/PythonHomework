def generate_squares(n):
    return {i: i**2 for i in range(1, n + 1)}


if __name__ == '__main__':
    assert generate_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, 'Test 1 failed'

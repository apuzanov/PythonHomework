def call_once(func):
    def wrapper(*args):
        if not wrapper.executed:
            wrapper.executed = True
            return func(*args)
    wrapper.executed = False
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == '__main__':
    assert sum_of_numbers(1, 2) == 3, 'Test 1 failed'
    assert sum_of_numbers(1, 2) is None, 'Test 2 failed'
    assert sum_of_numbers(2, 3) is None, 'Test 3 failed'

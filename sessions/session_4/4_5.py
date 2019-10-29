class remember_result:
    """It remembers last result of function it decorates and prints it before the next call"""
    def __init__(self, function):
        self.last_result = None
        self.function = function

    def __call__(self, *args, **kwargs):
        print(f"Last result = '{self.last_result}'")
        self.last_result = self.function(*args)


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
    print(f"Current result = '{result}'")
    return result


if __name__ == '__main__':
    sum_list("a", "b")
    sum_list("abc", "cde")

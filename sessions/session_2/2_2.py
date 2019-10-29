import re


def is_palindrome(s: str) -> bool:
    ns = re.sub(r'\W', '', str(s).lower())  # remove all not a word character
    return ns == ns[::-1]


if __name__ == '__main__':
    assert is_palindrome(10801) is True, 'Test 1 failed!'
    assert is_palindrome('madam ') is True, 'Test 2 failed!'
    assert is_palindrome('Madam, I\'m Adam') is True, 'Test 3 failed!'
    assert is_palindrome('A man, a plan, a canal, Panama!') is True, 'Test 4 failed!'



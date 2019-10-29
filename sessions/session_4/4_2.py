import re, collections


def most_common_words(filepath, number_of_words=3):
    with open(filepath) as f:
        words = [w.lower() for w in re.findall(r'[\w]+', f.read())]  # obtain all words
        return [t[0] for t in collections.Counter(words).most_common(number_of_words)]


if __name__ == '__main__':
    assert most_common_words(r'data/lorem_ipsum.txt') == ['donec', 'etiam', 'aliquam'], 'Test 1 failed'

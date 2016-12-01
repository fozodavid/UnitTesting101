from collections import defaultdict


def vowelsCheck(string):
    if not isinstance(string, str):
        raise TypeError

    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    result_dict = defaultdict(int)

    for letter in string.lower():
        if letter in vowels:
            result_dict[letter] += 1
        elif letter in consonants:
            result_dict['consonants'] += 1
    return dict(result_dict)

"""CSC108/CSCA08: Winter 2023 -- Assignment 1: Question Bot - Helper Functions

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Paul Gries, Sophia Huynh, Kaveh Mahdaviani, and Sadia Sharmin

====

The following functions are tools we created to make your A1 programming lives
easier. You should not modify this file.

Note that they use course material that you'll see in the coming weeks.
You can and should call them in your program; they'll do a lot of the
tricky work for you.

Read the docstrings and doctests to see how to use them — you only need to
understand the data that comes in and the data that comes out, not how the
code inside the function works.
"""

SPACE = ' '
EMPTY_STRING = ''


def get_lowercase_version(s: str) -> str:
    """Return a copy of s that is all lowercase.

    >>> get_lowercase_version('Hello There BOB!')
    'hello there bob!'
    >>> get_lowercase_version('computer')
    'computer'
    """

    return s.lower()


def get_uppercase_version(s: str) -> str:
    """Return a copy of s that is all uppercase.

    >>> get_uppercase_version('Hello There BOB!')
    'HELLO THERE BOB!'
    >>> get_uppercase_version('LOL')
    'LOL'
    """

    return s.upper()


def get_capitalized_word(word: str) -> str:
    """Return a copy of word that is capitalized - the first character is
    uppercase and the rest of the characters are unchanged.

    Precondition: word[0] is alphabetical

    >>> get_capitalized_word('baheN?')
    'BaheN?'
    >>> get_capitalized_word('Tom')
    'Tom'
    """

    return get_uppercase_version(word[0]) + word[1:]


def get_uncapitalized_word(word: str) -> str:
    """Return a copy of word where the first character is
    lowercase and the rest of the characters are unchanged.

    Precondition: word[0] is alphabetical

    >>> get_uncapitalized_word('Bahen?')
    'bahen?'
    >>> get_uncapitalized_word('noOdles')
    'noOdles'
    """

    return get_lowercase_version(word[0]) + word[1:]


def get_substring_index(sentence: str, substring: str) -> int:
    """Return the index of the leftmost occurrence of substring in sentence, or
    -1 if substring not in sentence.

    Precondition: sentence is a properly-formed English sentence

    >>> get_substring_index('The dog ate my homework, eh?', ' ')
    3
    >>> get_substring_index('The dog ate my homework, eh?', 'dog')
    4
    >>> get_substring_index('She used all my ketchup too.', 'dog')
    -1
    """

    return sentence.find(substring)


def drop_first_word(sentence: str) -> str:
    """Return a copy of sentence with the first word and its trailing space
    and/or trailing punctuation removed.

    Precondition: sentence is a properly-formed English sentence

    >>> drop_first_word('The dog ate my homework!')
    'dog ate my homework!'
    >>> drop_first_word('Tom, who ate my homework?')
    'who ate my homework?'
    >>> drop_first_word('homework!')
    ''
    """

    first_space_index = get_substring_index(sentence, SPACE)
    if first_space_index == -1:
        # There is only one word.
        return EMPTY_STRING
    else:
        return sentence[first_space_index + 1:]


def get_word(sentence: str, word_number: int) -> str:
    """Return the word in sentence that corresponds with word_number.
    A 0 indicates the first word in the sentence.

    Precondition: sentence is a properly-formed English sentence

    >>> get_word('The dog ate my homework!', 0)
    'The'
    >>> get_word('The dog ate my homework!', 1)
    'dog'
    """

    if word_number > count_words(sentence):
        return EMPTY_STRING
    split_sentence = sentence.split(' ')
    return split_sentence[word_number]


def count_words(sentence: str) -> int:
    """Return the number of words in sentence.

    Precondition: sentence is a properly-formed English sentence

    >>> count_words('The dog?')
    2
    >>> count_words('The dog ate my homework!')
    5
    """

    return sentence.count(SPACE) + 1


def get_first_word(sentence: str) -> str:
    """Return the first word in sentence.

    Precondition: sentence is a properly-formed English sentence
                    that is at least one word long.

    >>> get_first_word('The quick brown fox')
    'The'
    >>> get_first_word('Has the dog eaten my homework?')
    'Has'
    """

    first_space_index = get_substring_index(sentence, SPACE)
    if first_space_index == -1:
        # This must be the last word because there are no spaces left.
        # Get rid of the trailing punctuation.
        return sentence[: -1]
    else:
        return sentence[: first_space_index]


def get_last_word(sentence: str) -> str:
    """Return the last word in sentence, without the trailing punctuation
    character.

    Precondition: sentence is a properly-formed English sentence
                    that is at least one word long.

    >>> get_last_word('The quick brown fox.')
    'fox'
    >>> get_last_word('Has the dog eaten my homework?')
    'homework'
    """

    first_space_index = sentence.rfind(SPACE)
    if first_space_index == -1:
        # A single word. Remove the trailing punctuation.
        return sentence[: -1]
    else:
        return sentence[first_space_index + 1: -1]


if __name__ == '__main__':

    import doctest
    doctest.testmod()

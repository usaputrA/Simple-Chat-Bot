"""CSC108/CSCA08: Winter 2023 -- Assignment 1: Question Bot

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2023 Paul Gries, Sophia Huynh, Kaveh Mahdaviani, and Sadia Sharmin

====

This module has the code for a simple chatbot that rephrases questions
as statements and statements as questions.

Load the program into the Python shell by clicking the green triangle
in Wing101. Then you can chat as follows at the Python shell.

>>> chat('The dog ate my homework!')
'Homework is a meme.'
"""

# This tells Python to give us access to the functions in chat_utilities.py.
from chat_utilities import *

# Whether to run doctests. See the bottom of this file to see it in action.
DOCTEST_MODE = True

# Punctuation.
SEPARATOR = '|'
SPACE = ' '
PERIOD = '.'
QUESTION_SYMBOL = '?'
EXCLAMATION_SYMBOL = '!'

# Key terms.
HOMEWORK_KEYWORD = 'homework'

# A list of helping verbs.
HELPING_VERBS = '|have|has|had|should|would|could|might|may|will|' + \
                'is|am|are|was|be|do|does|did|'

# Special Canadian words.
CANADIAN_WORD_1 = 'snow'
CANADIAN_WORD_2 = 'ice'
CANADIAN_WORD_3 = 'hockey'

# Question words that start a sentence.
QUESTION_KEYWORD_1 = 'Will'
QUESTION_KEYWORD_2 = 'Can'

# Response fragments.
HOMEWORK_RESPONSE = 'Homework is a meme.'

EXCLAMATION_RESPONSE = ' ate my homework.'

CANADIAN_RESPONSE = ', eh?'

QUESTION_RESPONSE_0A = 'Is '
QUESTION_RESPONSE_0B = ' the homework topic?'

QUESTION_RESPONSE_1 = 'The future is opaque.'

QUESTION_RESPONSE_2A = ' is as '
QUESTION_RESPONSE_2B = ' does.'

QUESTION_RESPONSE_3A = 'Why do you say "'
QUESTION_RESPONSE_3B = '" and "'
QUESTION_RESPONSE_3C = '"?'

# None of the above
OTHERS = 'What do you mean?'


####################################
# TASK 1.1: Homework-related Inputs
# Complete the docstring examples below.
# You do not have to write any code for this task, but rather, read
# the code we have provided, understand it, and pay attention to our
# use of constants. You are expected to use constants accordingly, when
# appropriate, for the rest of the tasks.
####################################

def contains_homework(sentence: str) -> bool:
    """Return whether `sentence` contains the word 'homework' HOMEWORK_KEYWORD, 
    regardless of case.

    >>> contains_homework('The dog has eaten my Homework!')
    True
    >>> contains_homework('The dog has eaten my lunch!')
    False
    >>> contains_homework('The dog has eaten my hoMewOrK.')
    True
    """

    # Below, we are using the constant HOMEWORK_KEYWORD defined at the beginning
    # of this file, and the function get_lowercase_version which
    # we imported from chat_utilities.py
    return HOMEWORK_KEYWORD in get_lowercase_version(sentence)


def do_homework() -> str:
    """
    Return 'Homework is a meme.'

    >>> do_homework()
    'Homework is a meme.'
    """

    return HOMEWORK_RESPONSE


####################################
# TASK 2: Exclamations
####################################

def is_exclamation(sentence: str) -> bool:
    """ Return True iff `sentence` ends with an exclamation mark 
    EXCLAMATION_SYMBOl, and False otherwise.
    
    >>> is_exclamation("I don't want you!")
    True
    >>> is_exclamation("I don't want you.")
    False
    """
    return EXCLAMATION_SYMBOL in sentence[-1]


def do_exclamation(sentence: str) -> str:
    """ Return a string of the last word of `sentence`, capitalized,
    followed by EXCLAMATION_RESPONSE.
    
    Precondition: `is_exclamation` has to be True
    
    >>> do_exclamation("I don't want you!")
    'You ate my homework.'
    >>> do_exclamation("Don't do that!")
    'That ate my homework.'
    """
    capitalized_last_word = get_capitalized_word(get_last_word(sentence))
    return capitalized_last_word + EXCLAMATION_RESPONSE


####################################
# TASK 3: Helping Verbs
####################################

# The following helper function is already completed for you
# Do not add or change anything in this function
def is_helping_verb(word: str) -> bool:
    """
    Return whether word is a lowercase helping verb in HELPING_VERBS.
    Every word in HELPING_VERBS is surrounded by SEPARATOR characters,
    for example '|will|'.

    >>> is_helping_verb('do')
    True
    >>> is_helping_verb('i')
    False
    """

    return (SEPARATOR + word + SEPARATOR) in HELPING_VERBS


def contains_helping_verb(sentence: str) -> bool:
    """ Return True iff `sentence` have at least three words, ends a period 
    PERIOD, and contains a lowercase helping verb in HELPING_VERBS as its 
    third word, False otherwise.
    
    >>> contains_helping_verb('The dog has eaten my notes.')
    True
    >>> contains_helping_verb('The big dog has eaten my notes.')
    False
    >>> contains_helping_verb('The big.')
    False
    """
    count = count_words(sentence) >= 3    
    if count:
        third_word = get_word(sentence, 2)
        help_verb = is_helping_verb(third_word)
        return help_verb and (count and PERIOD in sentence[-1])
    return count


def do_helping_verb(sentence: str) -> str:
    """ Return a string of `sentence` with the helping verb in HELPING_VERBS 
    is capitalized and moved to the front, followed by the original 
    first letter of `sentence` that become a lowercase, and the the period 
    PERIOD at the end of the sentence is being replaced by a question mark 
    QUESTION_SYMBOL.
    
    Precondition: `contains_helping_verb` has to be True
    
    >>> do_helping_verb('The dog has eaten my notes.')
    'Has the dog eaten my notes?'
    >>> do_helping_verb('Poor Clara had slept through her test.')
    'Had poor Clara slept through her test?'
    >>> do_helping_verb('TrickY Henry had tricked me.')
    'Had trickY Henry tricked me?'
    """
    # Make the first letter of the sentence lettercase and remove the dot
    new_sentence = get_uncapitalized_word(sentence[:-1])
    
    # Divide sentence into two parts, the first half:
    third_word = get_word(new_sentence, 2)
    third_index = get_substring_index(new_sentence, third_word) 
    first_half = new_sentence[:third_index]
    
    # Now work for the second half:
    third_length = len(third_word)
    
    # Added by 1 because function len doesn't count the index from zero
    second_half_index = third_index + third_length + 1 
    second_half = new_sentence[second_half_index:]
    
    capitalized = get_capitalized_word(third_word)
    
    return capitalized + SPACE + first_half + second_half + QUESTION_SYMBOL


####################################
# TASK 4: Canadian
####################################


def is_canadian_question(sentence: str) -> bool:
    """ Return whether `sentence` contains CANADIAN_WORD_1 or CANADIAN_WORD_2 
    or CANADIAN_WORD_3 and ends with QUESTION_SYMBOL.
    
    >>> is_canadian_question("Is it snowing outside?")
    True
    >>> is_canadian_question("Is it Snowing outside?")
    False
    >>> is_canadian_question("It is snowing outside.")
    False
    """
    CA_1 = CANADIAN_WORD_1 in sentence
    CA_2 = CANADIAN_WORD_2 in sentence
    CA_3 = CANADIAN_WORD_3 in sentence
    return (CA_1 or CA_2 or CA_3) and (QUESTION_SYMBOL in sentence[-1])
    
    
def do_canadian_question(sentence: str) -> str:
    """ Return a string of all letter of `sentence`, excluding the question 
    mark at the end of `sentence`, followed by CANADIAN_RESPONSE.
    
    Precondition: `is_canadian_word` has to be True
    
    >>> do_canadian_question('Is it snowing outside?')
    'Is it snowing outside, eh?'
    >>> do_canadian_question('Can you be nice a bit?')
    'Can you be nice a bit, eh?'
    """
    return sentence[:-1] + CANADIAN_RESPONSE
        

####################################
# TASK 5: Questions
####################################


def is_question(sentence: str) -> bool:
    """ Return True iff `sentence` ends with a QUESTION_SYMBOL.
    
    >>> is_question("Hungry?")
    True
    >>> is_question("Yes? You think the pictures are awesome!")
    False
    """
    return QUESTION_SYMBOL in sentence[-1]


def do_question(sentence: str) -> str:
    """ Return a string with QUESTION_RESPONSE_0A, followed by the lowercase 
    `sentence`, 
    followed by QUESTION_RESPONSE_0B if `sentence` contains 
    only 1 word
    
    Return a string QUESTION_RESPONSE_1 if `sentence` contains 
    QUESTION_KEYWORD_1
    
    Return a string with a capitalized last word of `sentence`, 
    followed by QUESTION_RESPONSE_2A, 
    followed by the last word of `sentence`, 
    followed by QUESTION_RESPONSE_2B if `sentence` contains QUESTION_KEYWORD_2
    
    Return a string QUESTION_RESPONSE_3A followed by the second word of 
    `sentence`, 
    followed by QUESTION_RESPONSE_3C if the last word and second word of 
    `sentence` are the same, regardless the case
    
    Return a string QUESTION_RESPONSE_3A followed by the second word of 
    `sentence`, 
    followed by QUESTION_RESPONSE_3B, 
    followed by the last word of `sentence`,
    followed by QUESTION_RESPONSE_3C if the last word and second word of 
    `sentence` are not the same
    
    Precondition: `is_question` has to be True
    
    >>> do_question("Yes! Do you think the pictures are awesome?")
    'Why do you say "Do" and "awesome"?'
    >>> do_question("I know what you know?")
    'Why do you say "know"?'
    >>> do_question("Hungry?")
    'Is hungry the homework topic?'
    >>> do_question("Will you help me with the cleaning?")
    'The future is opaque.'
    >>> do_question("Can a dog go to the gym?")
    'Gym is as gym does.'
    """
    # If there's only 1 word
    uncapitalized = get_uncapitalized_word(sentence[:-1])
    if count_words(sentence) == 1:
        return QUESTION_RESPONSE_0A + uncapitalized + QUESTION_RESPONSE_0B
    
    # If the first word of the question is `Will` or `Can`, 
    elif QUESTION_KEYWORD_1 in sentence:
        return QUESTION_RESPONSE_1
    elif QUESTION_KEYWORD_2 in sentence:
        last = get_last_word(sentence)
        upper_last = get_capitalized_word(last)
        return upper_last + QUESTION_RESPONSE_2A + last + QUESTION_RESPONSE_2B
    else:
        second = get_word(sentence, 1)
        last = get_last_word(sentence)
        if get_lowercase_version(second) == get_lowercase_version(last):
            return QUESTION_RESPONSE_3A + second + QUESTION_RESPONSE_3C
        else:
            return 'Why do you say "' + second + '" and "' + last + '"?'
        
        
####################################
# TASK 6: Question Exclamations
####################################


def is_question_exclamation(sentence: str) -> bool:
    """ Return True iff `sentence` ends with a question exclamation symbol, 
    False otherwise.
    
    >>> is_question_exclamation("Will you study for the midterm?!")
    True
    >>> is_question_exclamation("Can a dog go to the gym??!")
    True
    >>> is_question_exclamation("Can a dog go to the gym?! Lol.")
    False
    """
    question = sentence[-2]
    exclamation = sentence[-1]
    return QUESTION_SYMBOL in question and EXCLAMATION_SYMBOL in exclamation


def do_question_exclamation(sentence: str) -> str:
    """ Return a string with the same output as `do_question` function because 
    this function will remove the exclamation mark from `sentence` to get a 
    string ending with only the question mark.
    
    Precondition: `is_question_exclamation` has to be True
    
    >>> do_question_exclamation("Will you study for the midterm?!")
    'The future is opaque.'
    >>> do_question_exclamation("Can a dog go to the gym?!")
    'Gym is as gym does.'
    """
    change = sentence[:-1]
    return do_question(change)
    
####################################
# TASK 8: None of the above
####################################


def do_unmatched() -> str:
    """ Return a string with a constant OTHERS
    
    >>> do_unmatched()
    'What do you mean?'
    """
    return OTHERS 


####################################
# Chat Functionality
####################################

# TASK 7: Make sure the chat function has the correct order for all checks
def chat(sentence: str) -> str:
    """Return a question if `sentence` is a statement or exclamation, and
    return a statement if `sentence` is a question.

    >>> chat('The dog ate my homework!')
    'Homework is a meme.'
    >>> chat('The thing is due tomorrow!')
    'Tomorrow ate my homework.'
    >>> chat('The dog has eaten my shoe.')
    'Has the dog eaten my shoe?'
    >>> chat('You watching the hockey game?')
    'You watching the hockey game, eh?'
    >>> chat('How much wood could a woodchuck chuck?')
    'Why do you say "much" and "chuck"?'
    >>> chat("Yes! Don't you think the pictures are awesome?")
    'Why do you say "Don\\'t" and "awesome"?'
    """

    if contains_homework(sentence):
        return do_homework()
    elif is_question_exclamation(sentence):
        return do_question_exclamation(sentence)    
    elif is_exclamation(sentence):
        return do_exclamation(sentence)
    elif contains_helping_verb(sentence):
        return do_helping_verb(sentence)
    elif is_canadian_question(sentence):
        return do_canadian_question(sentence)
    elif is_question(sentence):
        return do_question(sentence)
    else:
        return do_unmatched()
    
    
if __name__ == '__main__':

    if DOCTEST_MODE:
        import doctest
        doctest.testmod()

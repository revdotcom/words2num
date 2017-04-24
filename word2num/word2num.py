"""Denormalize numbers, given normalized input.
"""
import re


SHORT_SCALE_ENGLISH = {
    'vocab': {
        'zero': (0, 'Z'),
        'a': (1, 'D'),
        'one': (1, 'D'),
        'two': (2, 'D'),
        'three': (3, 'D'),
        'four': (4, 'D'),
        'five': (5, 'D'),
        'six': (6, 'D'),
        'seven': (7, 'D'),
        'eight': (8, 'D'),
        'nine': (9, 'D'),
        'ten': (10, 'M'),
        'eleven': (11, 'M'),
        'twelve': (12, 'M'),
        'thirteen': (13, 'M'),
        'fourteen': (14, 'M'),
        'fifteen': (15, 'M'),
        'sixteen': (16, 'M'),
        'seventeen': (17, 'M'),
        'eighteen': (18, 'M'),
        'nineteen': (19, 'M'),
        'twenty': (20, 'T'),
        'thirty': (30, 'T'),
        'forty': (40, 'T'),
        'fifty': (50, 'T'),
        'sixty': (60, 'T'),
        'seventy': (70, 'T'),
        'eighty': (80, 'T'),
        'ninety': (90, 'T'),
        'hundred': (100, 'H'),
        'thousand': (10**3, 'X'),
        'million': (10**6, 'X'),
        'billion': (10**9, 'X'),
        'trillion': (10**12, 'X'),
        'quadrillion': (10**15, 'X'),
        'quintillion': (10**18, 'X'),
        # 'sextillion': (10**21, 'X'),
        # 'septillion': (10**24, 'X'),
        # 'octillion': (10**27, 'X'),
        # 'nonillion': (10**30, 'X'),
        # 'decillion': (10**33, 'X'),
        # 'undecillion': (10**36, 'X'),
        # 'duodecillion': (10**39, 'X'),
        # 'tredecillion': (10**42, 'X'),
        # 'quattuordecillion': (10**45, 'X'),
        # 'quindecillion': (10**48, 'X'),
        # 'sexdecillion': (10**51, 'X'),
        # 'septendecillion': (10**54, 'X'),
        # 'octodecillion': (10**57, 'X'),
        # 'novemdecillion': (10**60, 'X'),
        # 'vigintillion': (10**63, 'X'),
        # 'centillion': (10**303, 'X'),
    },
}

LANG = {'en_us': SHORT_SCALE_ENGLISH}


class NumberException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


def tokenize(text, vocab):
    tokens = re.split(r"[\s,\-]+(?:and)?", text.lower())
    try:
        result = ([vocab[token] for token in tokens if token])
    except KeyError as e:
        raise NumberException("Invalid number word: "
                              "{0} in '{1}'".format(e, text))
    return result


def compute(acc, tokens):
    if len(tokens) == 0:
        return acc

    (value_next, type_next), tokens_remaining = tokens[0], tokens[1:]
    if type_next in {'D', 'M', 'T'}:
        return compute(acc + value_next, tokens_remaining)
    elif type_next in {'H'}:
        return compute(acc * value_next, tokens_remaining)
    elif type_next in {'X'}:
        return acc * value_next + compute(0, tokens_remaining)
    else:
        raise NumberException("Unable to process token: "
                              "{0}({1})'".format(value_next, type_next))


def word2num(text):
    vocab = LANG['en_us']['vocab']
    tokens = tokenize(text, vocab)
    return compute(0, tokens)

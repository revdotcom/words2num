"""Denormalize numbers, given normalized input.
"""


def w2n(text):
    from .lang_EN_US import evaluate
    return evaluate(text)

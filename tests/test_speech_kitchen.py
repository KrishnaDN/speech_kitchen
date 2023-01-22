import numpy as np
from collections import Counter
from speech_kitchen.speech_kitchen import count_words

def test_count_words():
    expected = Counter({'insanity': 1, 'is': 1, 'doing': 1,
        'the': 1, 'same': 1, 'thing': 1,
        'over': 2, 'and': 2, 'expecting': 1,
        'different': 1, 'results': 1})

    actual = count_words("tests/einstein.txt")
    assert actual == expected
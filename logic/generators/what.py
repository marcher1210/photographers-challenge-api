from .abstract import SetLimitGenerator
from datetime import date, timedelta
from random import randrange

import json

import sys

word_json_local = "assets/words.json"

class WordLimitGenerator(SetLimitGenerator[str]):
    def __init__(self, seed = None) -> None:
        s = json.loads(open(word_json_local, mode='r').read())
        tuples = s['data']
        s = [t['word'] for t in tuples]
        SetLimitGenerator.__init__(self, s, seed)
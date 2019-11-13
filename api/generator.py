from logic.generators.when import DateLimitGenerator, TimeLimitGenerator
from logic.generators.what import WordLimitGenerator
from logic.generators.general import *
from werkzeug import ImmutableMultiDict
from datetime import date, time




def GET_numbers(lowerBound: int, upperBound: int, n: int, type: str = 'sequential', seed: int = None):
    gen = IntLimitGenerator(lowerBound=lowerBound, upperBound=upperBound, seed=seed)
    seed = gen.getSeed()
    data = gen.generateRandomList(n) if type=='random' else gen.generateSequentialList(n) 

    resp = {}
    resp['seed'] = seed
    resp['data'] = data
    return {
        "success": True,
        "response": resp,
        }


def GET_dates(lowerBound: date, upperBound: date, n: int, type: str = 'sequential', seed: int = None):
    gen = DateLimitGenerator(lowerBound=lowerBound, upperBound=upperBound, seed=seed)
    seed = gen.getSeed()
    data = gen.generateRandomList(n) if type=='random' else gen.generateSequentialList(n) 

    resp = {}
    resp['seed'] = seed
    resp['data'] = data
    return {
        "success": True,
        "response": resp,
        }

def GET_times(lowerBound: time, upperBound: time, n: int, type: str = 'sequential', seed: int = None):
    gen = TimeLimitGenerator(lowerBound=lowerBound, upperBound=upperBound, seed=seed)
    seed = gen.getSeed()
    data = gen.generateRandomList(n) if type=='random' else gen.generateSequentialList(n) 

    resp = {}
    resp['seed'] = seed
    resp['data'] = data
    return {
        "success": True,
        "response": resp,
        }


def GET_words(n: int, seed: int = None):
    gen = WordLimitGenerator(seed)    
    
    seed = gen.getSeed()
    words = gen.generateRandomList(n)

    resp = {}
    resp['seed'] = seed
    resp['words'] = words
    return {
        "success": True,
        "response": resp,
        }

if __name__ == "__main__":
    print("yea")
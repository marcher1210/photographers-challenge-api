from logic.generators.when import DateLimitGenerator, TimeLimitGenerator
from logic.generators.what import WordLimitGenerator
from logic.generators.general import *
from werkzeug import ImmutableMultiDict
from datetime import date, time




def numbers(args : ImmutableMultiDict):
    lowerBound = int(args['lowerBound'])
    upperBound = int(args['upperBound'])
    if args.get('seed'):
        gen = IntLimitGenerator(
            lowerBound=lowerBound,
            upperBound=upperBound,
            seed=args.get('seed', type=int)
            )
    else:
        gen = IntLimitGenerator(
            lowerBound=lowerBound,
            upperBound=upperBound)
    seed = gen.getSeed()
    data = gen.generateRandomList(args.get('n', type=int)) if args.get("type")=='random' else gen.generateSequentialList(args.get('n', type=int)) 

    resp = {}
    resp['seed'] = seed
    resp['data'] = data
    return {
        "request": args,
        "success": True,
        "response": resp,
        }


def dates(args : ImmutableMultiDict):
    lowerBound = date.fromisoformat(args['lowerBound'])
    upperBound = date.fromisoformat(args['upperBound'])
    if args.get('seed'):
        gen = DateLimitGenerator(
            lowerBound=lowerBound,
            upperBound=upperBound,
            seed=args.get('seed', type=int)
            )
    else:
        gen = DateLimitGenerator(
            lowerBound=lowerBound,
            upperBound=upperBound)
    seed = gen.getSeed()
    dates = gen.generateRandomList(args.get('n', type=int)) if args.get("type")=='random' else gen.generateSequentialList(args.get('n', type=int)) 

    resp = {}
    resp['seed'] = seed
    resp['dates'] = dates
    return {
        "request": args,
        "success": True,
        "response": resp,
        }

def times(args : ImmutableMultiDict):
    lowerBound = time.fromisoformat(args['lowerBound'])
    upperBound = time.fromisoformat(args['upperBound'])
    if args.get('seed'):
        gen = TimeLimitGenerator(
            lowerBound=lowerBound,
            upperBound=upperBound,
            seed=args.get('seed', type=int)
            )
    else:
        gen = TimeLimitGenerator(
            lowerBound=lowerBound,
            upperBound=upperBound)
    seed = gen.getSeed()
    times = gen.generateRandomList(args.get('n', type=int)) if args.get("type")=='random' else gen.generateSequentialList(args.get('n', type=int)) 

    resp = {}
    resp['seed'] = seed
    resp['times'] = times
    return {
        "request": args,
        "success": True,
        "response": resp,
        }


def words(args : ImmutableMultiDict):
    if args.get('seed'):
        gen = WordLimitGenerator(seed=args.get('seed', type=int))
    else:
        gen = WordLimitGenerator()
    
    seed = gen.getSeed()
    words = gen.generateRandomList(args.get('n', type=int))

    resp = {}
    resp['seed'] = seed
    resp['words'] = words
    return {
        "request": args,
        "success": True,
        "response": resp,
        }

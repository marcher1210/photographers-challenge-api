from logic.generators.abstract import SequenceLimitGenerator, RandomLimitGenerator
from logic.generators.when import DateLimitGenerator, TimeLimitGenerator
from logic.generators.what import WordLimitGenerator
from logic.generators.where import CoordinateLimitGenerator
from logic.generators.general import *
from logic.render.map import *

from werkzeug import ImmutableMultiDict
from datetime import date, time



def generate_sequence_response(generator: SequenceLimitGenerator, n: int):
    items = generator.generateSequentialList(n)

    return {
        "items": items,
        }

def generate_random_response(generator: RandomLimitGenerator, n: int):
    seed = generator.getSeed()
    items = generator.generateRandomList(n)

    return {
        "seed": seed,
        "items": items,
        }

## Sequence

def GET_sequence_numbers(lowerBound: int, upperBound: int, n: int):
    generator = IntLimitGenerator(lowerBound=lowerBound, upperBound=upperBound)
    return generate_sequence_response(generator, n)

def GET_sequence_dates(lowerBound: date, upperBound: date, n: int):
    generator = DateLimitGenerator(lowerBound=lowerBound, upperBound=upperBound)
    return generate_sequence_response(generator, n)

def GET_sequence_times(lowerBound: time, upperBound: time, n: int):
    generator = TimeLimitGenerator(lowerBound=lowerBound, upperBound=upperBound)
    return generate_sequence_response(generator, n)


## Random

def GET_random_numbers(lowerBound: int, upperBound: int, n: int, seed: int):
    generator = IntLimitGenerator(lowerBound=lowerBound, upperBound=upperBound, seed=seed)
    return generate_random_response(generator, n)

def GET_random_dates(lowerBound: date, upperBound: date, n: int, seed: int):
    generator = DateLimitGenerator(lowerBound=lowerBound, upperBound=upperBound, seed=seed)
    return generate_random_response(generator, n)

def GET_random_times(lowerBound: time, upperBound: time, n: int, seed: int):
    generator = TimeLimitGenerator(lowerBound=lowerBound, upperBound=upperBound, seed=seed)
    return generate_random_response(generator, n)

def GET_random_words(n: int, seed: int):
    generator = WordLimitGenerator(seed)    
    return generate_random_response(generator, n)

def GET_random_coordinates(n: int, seed: int):
    generator = CoordinateLimitGenerator("assets/cph.kml",seed)    
    return generate_random_response(generator, n)

## Pages

def GET_pages( n: int, seed: int):
    generator = WordLimitGenerator(seed)    
    seed = generator.getSeed()
    words = generator.generateRandomList(n)

    generator = DateLimitGenerator(lowerBound=date(2019,2,17), upperBound=date(2090,1,1))
    dates = generator.generateSequentialList(n)

    generator = CoordinateLimitGenerator("assets/cph.kml",seed)
    coordinates = generator.generateRandomList(n)

    items = [
        {
            "what": words[i],
            "when": dates[i],
            "where": coordinates[i]
        } 
        for i in range(n)]
    return {
        "seed": seed,
        "items": items,
        }

## Render images

def GET_render_map_overview(lon: float, lat: float, boundMinLon: float, boundMinLat: float, boundMaxLon: float, boundMaxLat: float):
    return getOverviewMapResponse(lon, lat, boundMinLon, boundMinLat, boundMaxLon, boundMaxLat)

def GET_render_map_local(lon: float, lat: float):
    return getLocalMapResponse(lon, lat)

if __name__ == "__main__":
    print("yea")
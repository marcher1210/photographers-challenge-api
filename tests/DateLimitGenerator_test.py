
from logic.generators.when import DateLimitGenerator

from datetime import date

def test_length():
    gen = DateLimitGenerator(date(2019,11,1), date(2019,11,10))
    assert len(gen.generateSequentialList(20)) == 20

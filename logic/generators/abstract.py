from abc import ABC, abstractmethod
from random import Random, randrange
from datetime import date, timedelta
import sys

from typing import TypeVar, Generic, List, Set, Iterable
T = TypeVar('T')

class LimitGenerator(ABC, Generic[T]):
    pass


class RandomLimitGenerator(LimitGenerator[T]):
    def __init__(self, seed=None) -> None:
        if seed == None:
            self.seed = randrange(sys.maxsize)
        else:
            self.seed = seed
        self.rand = Random(seed)

    def getSeed(self):
        return self.seed
    
    def reset(self):
        self.rand = Random(self.seed)

    def generateRandomN(self, n : int) -> Iterable[T]:
        for i in range(n):
            yield self.generateRandomOne() 

    def generateRandomList(self, n : int) -> List[T]:
        return [l for l in self.generateRandomN(n)]

    @abstractmethod
    def generateRandomOne(self) -> T:
        pass
 
class SequentialLimitGenerator(LimitGenerator[T]):
    def __init__(self, start : T) -> None:
        self.currentItem = start
    
    def setCurrent(newCurrent : T) -> None:
        self.currentItem = newCurrent

    def generateSequentialN(self, n : int) -> Iterable[T]:
        for i in range(n):
            t = self.currentItem
            self.increment()
            yield t

    def generateSequentialList(self, n : int) -> List[T]:
        return [l for l in self.generateSequentialN(n)]

    @abstractmethod
    def increment(self) -> None:
        pass


class DiscreteLimitGenerator(RandomLimitGenerator[T]):
    pass


class BoundsLimitGenerator(DiscreteLimitGenerator[T], SequentialLimitGenerator[T]):
    def __init__(self, lowerBound : T, upperBound : T, seed=None) -> None:
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        SequentialLimitGenerator.__init__(self, lowerBound)
        DiscreteLimitGenerator.__init__(self, seed)


class SetLimitGenerator(DiscreteLimitGenerator[T]):
    def __init__(self, limitSet : Set[T], seed=None) -> None:
        self.limitSet = limitSet
        super().__init__(seed)

    def generateRandomOne(self) -> T:
        return self.rand.choice(self.limitSet)

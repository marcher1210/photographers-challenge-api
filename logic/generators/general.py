from .abstract import BoundsLimitGenerator

class IntLimitGenerator(BoundsLimitGenerator[int]):
    def increment(self):
        self.currentItem = self.currentItem + 1
        if self.currentItem > self.upperBound:
            self.currentItem = self.lowerBound

    def generateRandomOne(self) -> int:
        return self.rand.randint(self.lowerBound,self.upperBound)


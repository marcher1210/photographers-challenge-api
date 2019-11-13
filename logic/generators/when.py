from .abstract import SequentialLimitGenerator, BoundsLimitGenerator

from datetime import datetime, date, time, timedelta

class DateLimitGenerator(BoundsLimitGenerator[date]):
    def increment(self):
        self.currentItem = self.currentItem + timedelta(days=1)
        if self.currentItem > self.upperBound:
            self.currentItem = self.lowerBound
    
    def generateRandomOne(self) -> date:
        delta = self.upperBound - self.lowerBound
        days = delta.days
        rDays = self.rand.randint(0, days)
        return self.lowerBound + timedelta(days=rDays)



class TimeLimitGenerator(BoundsLimitGenerator[time]):
    def increment(self):
        self.currentItem = (datetime.combine(date(1, 1, 1), self.currentItem) + timedelta(minutes=1)).time()
        if self.currentItem > self.upperBound:
            self.currentItem = self.lowerBound
    
    def generateRandomOne(self) -> time:
        delta = datetime.combine(date(1, 1, 1), self.upperBound) - datetime.combine(date(1, 1, 1), self.lowerBound)
        mins = delta.seconds / 60
        rMins = self.rand.randint(0, mins)
        return (datetime.combine(date(1, 1, 1), self.lowerBound) + timedelta(minutes=rMins)).time()


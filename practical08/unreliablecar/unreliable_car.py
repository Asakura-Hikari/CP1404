from practical08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliability = random.randint(1, 100)
        if self.reliability < reliability:
            super().drive(distance)
        else:
            print("Car refuses to run!!!!")
            return distance

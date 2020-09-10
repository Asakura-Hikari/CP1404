from practical08.taxi.taxi import Taxi

FLAG = 4.5


class SilverServiceTaxi(Taxi):
    flagfall = FLAG

    def __init__(self, name, fuel, price_per_km):
        super().__init__(name, fuel)
        self.price_per_km = price_per_km

    def __str__(self):
        return super().__str__() + "plus flagfall of {}".format(SilverServiceTaxi.flagfall)

    def get_fare(self):
        return super().get_fare() + SilverServiceTaxi.flagfall

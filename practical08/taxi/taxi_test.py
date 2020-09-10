from practical08.taxi.taxi import Taxi


def main():
    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi)
    new_taxi.start_fare()
    new_taxi.add_fuel(40)
    new_taxi.drive(100)
    print(new_taxi)
    print("The current fare is {}".format(new_taxi.get_fare()))


if __name__ == '__main__':
    main()

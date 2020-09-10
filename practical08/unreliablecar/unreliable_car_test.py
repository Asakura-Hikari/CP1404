from practical08.unreliablecar.unreliable_car import UnreliableCar


def main():
    new_car = UnreliableCar("Audi", 100, 50)
    new_car.drive(50)
    print(new_car)


if __name__ == '__main__':
    main()

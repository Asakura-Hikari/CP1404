from practical08.SliverServiceTaxi.SilverServiceTaxi import SilverServiceTaxi


def main():
    Hummer = SilverServiceTaxi("Hummer", 200, 4.92)
    Hummer.drive(18)
    print(Hummer)
    print(Hummer.get_fare())


if __name__ == '__main__':
    main()

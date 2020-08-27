from practical06.Guitar.guitar import Guitar


def main():
    Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    Another = Guitar("Another Guitar", 2013, 12312.30)

    print("{} get_age() - Expected 98. Got {}".format(Gibson.name, Gibson.get_age()))
    print("{} get_age() - Expected 98. Got {}".format(Another.name, Another.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(Gibson.name, Gibson.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(Another.name, Another.is_vintage()))


if __name__ == '__main__':
    main()

from practical06.Guitar.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    add_guitar(guitars)
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            print(
                "Guitar {}: {} ({}), worth ${.2f}(vintage)".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                   ))
        else:
            print(
                "Guitar {}: {} ({}), worth ${.2f}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                          ))


def add_guitar(guitars):
    var = True
    while var:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : ${} added.".format(name, year, cost))


if __name__ == '__main__':
    main()

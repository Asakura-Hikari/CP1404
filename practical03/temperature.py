def main():
    C = get_celsius()
    F = temp_change(C)
    print("{:,.2f} Celsius is ${:,.2f} Fahrenheit".format(C, F))


def get_celsius():
    C = input("Please enter celsius temperature:")
    return float(C)


def temp_change(C):
    F = C * 1.8 + 32
    return F


if __name__ == '__main__':
    main()

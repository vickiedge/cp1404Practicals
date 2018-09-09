from prac_06.guitar import Guitar


def run_tests():
    Gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    Another = Guitar("Another", 2012, 100)

    guitars = [Gibson, Another]
    # for guitar in guitars:
    #   print("{} get_age() - Expected {}. Got  {}".format(guitar.name, "95", guitar.get_age()))

    print("{} get_age() - Expected {}. Got {}".format(Gibson.name, 96, Gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(Another.name, 6, Another.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(Gibson.name, True, Gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(Another.name, False, Another.is_vintage()))


if __name__ == "__main__":
    run_tests()

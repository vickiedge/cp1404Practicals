from prac_06.guitar import Guitar
# from operator import itemgetter


def main():
    """Guitar program, using Guitar class."""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # guitars.sort(key=itemgetter(0))
    print("These are my guitars:")
    if len(guitars) != 0:
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
                print("Guitar {0}: {1.name:>20} ({1.year}),  worth  ${1.cost:10,.2f} {2}".format(i + 1, guitar,
                                                                                                 vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()

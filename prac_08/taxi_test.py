"""
CP1404/CP5632 Practical - Suggested Solution
Test taxi
"""

from prac_08.taxi import Taxi


def main():
    """Test Taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    fare = my_taxi.get_fare()
    print(my_taxi)
    print("${:.2f} fare cost".format(fare))
    my_taxi.start_fare()
    my_taxi.drive(100)
    fare = my_taxi.get_fare()
    print(my_taxi)
    print("${:.2f} fare cost".format(fare))



main()
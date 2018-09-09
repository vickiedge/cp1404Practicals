"""
Programming Guitar Class
"""

CURRENT_YEAR = 2018
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return desired printing format."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Return age of guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return if vintage"""
        return self.get_age() >= VINTAGE_AGE

"""
This module contains the BicycleManager class for managing a collection of bicycles.
"""

class BicycleManager:
    """A class for managing a collection of bicycles."""

    def __init__(self):
        """Initialize a BicycleManager object."""
        self.bicycles = []

    def add_bicycles(self, bicycle):
        """ Add a bicycle to the collection. """
        self.bicycles.append(bicycle)

    def find_bicycles_with_max_speed_more_than(self, max_speed):
        """ Find bicycles with a maximum speed greater than the given value. """
        return filter(lambda bicycle: bicycle.max_speed > max_speed, self.bicycles)

    def find_bicycles_by_brand(self, brand):
        """ Find bicycles by brand. """
        return filter(lambda bicycle: bicycle.brand == brand, self.bicycles)



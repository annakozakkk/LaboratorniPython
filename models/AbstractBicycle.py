from abc import ABC, abstractmethod


class AbstractBicycle(ABC):
    """An abstract base class representing a bicycle."""

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0):
        """Initialize an AbstractBicycle object."""
        self.__type_of_bicycle = type_of_bicycle
        self.__brand = brand
        self.__max_speed = max_speed
        self.__current_speed = current_speed

    @abstractmethod
    def get_max_distance(self):
        """
        Calculate and return the maximum distance the bicycle can travel.

        This method must be implemented by the derived classes.

        """
        pass

    @property
    def brand(self):
        """Get the brand of the bicycle."""
        return self.__brand

    @property
    def type_of_bicycle(self):
        """Get the type of the bicycle."""
        return self.__type_of_bicycle

    @property
    def max_speed(self):
        """  Get the maximum speed of the bicycle.  """
        return self.__max_speed

    @property
    def current_speed(self):
        """ Get the current speed of the bicycle. """
        return self.__current_speed

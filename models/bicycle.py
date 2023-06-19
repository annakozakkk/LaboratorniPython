"""
Bicycle Module

This module defines the Bicycle class that represents a bicycle object.
It provides functionality for accelerating,
braking and slowing down the bicycle, as well as printing the object's information.

Author: Anna
Date: May 16, 2023
"""
import sys
from abc import ABC


from models.abstract_bicycle import AbstractBicycle


class Bicycle(AbstractBicycle, ABC):
    """constructor of class"""

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0, the_best_qualities=None):
        super().__init__(type_of_bicycle, brand, max_speed, current_speed)
        self._the_best_qualities = the_best_qualities

    __instance = None

    @staticmethod
    def get_instance():
        """ get_instance = get the singleton instance of the Bicycle class."""
        if Bicycle.__instance is None:
            Bicycle.__instance = Bicycle()
        return Bicycle.__instance

    def accelerate(self, speed):
        """accelerate = accelerate the bicycle by thу specified speed"""
        if speed < self._max_speed:
            self.__current_speed += speed
            return self.__current_speed

        return self._max_speed



    def slow_down(self, speed):
        """slow_down = slow down the bicycle by the specified speed"""
        if speed <= self.__current_speed:
            self.__current_speed -= speed
            return self.__current_speed
        return self.brake()

    def __str__(self):
        """print objects by the specified pattern"""
        return f"{super().__str__()}"

    def get_max_distance(self):
        """Return the maximum distance the bicycle can travel."""
        return sys.maxsize

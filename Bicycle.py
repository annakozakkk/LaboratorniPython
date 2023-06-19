"""
Bicycle Module

This module defines the Bicycle class that represents a bicycle object. It provides functionality for
accelerating, braking and slowing down the bicycle, as well as printing the object's information.

Author: Anna
Date: May 16, 2023
"""


class Bicycle:
    """constructor of class"""

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0):
        self.__type_of_bicycle = type_of_bicycle
        self.__brand = brand
        self.__max_speed = max_speed
        self.__current_speed = current_speed

    __instance = None

    @staticmethod
    def get_instance():
        """ get_instance = get the singleton instance of the Bicycle class."""
        if Bicycle.__instance is None:
            Bicycle.__instance = Bicycle()
        return Bicycle.__instance

    def accelerate(self, speed):
        """accelerate = accelerate the bicycle by thу specified speed"""
        if speed < self.__max_speed:
            self.__current_speed += speed
            return self.__current_speed

        return self.__max_speed

    def brake(self):
        """brake = stop the bicycle"""
        self.__current_speed = 0
        return self.__current_speed

    def slow_down(self, speed):
        """slow_down = slow down the bicycle by the specified speed"""
        if speed <= self.__current_speed:
            self.__current_speed -= speed
            return self.__current_speed
        return self.brake()

    def __str__(self):
        """print objects by the specified pattern"""
        return f"Bicycle: type={self.__type_of_bicycle}, brand={self.__brand}, " \
               f"maxSpeed={self.__max_speed}, currentSpeed={self.__current_speed}"


bicycles = [Bicycle("road", "Trek", 40, 23), Bicycle(), Bicycle.get_instance(), Bicycle.get_instance()]

for bicycle in bicycles:
    print(bicycle)

list_1 = list(range(50))
list_2 = []
new_list = [k + k for k in list_1[1::2]]
print(new_list)

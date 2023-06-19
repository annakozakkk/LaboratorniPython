from models.AbstractBicycle import AbstractBicycle


class ElectricScooter(AbstractBicycle):
    """A class representing an electric scooter, derived from AbstractBicycle."""

    def __init__(self, type_of_bicycle="None", brand="None", max_speed=0, current_speed=0,
                 time_to_drive_on_battery_charge=0, average_speed=0):
        """ Initialize an ElectricScooter object."""
        super().__init__(type_of_bicycle, brand, max_speed, current_speed)
        self.__time_to_drive_on_battery_charge = time_to_drive_on_battery_charge
        self.__average_speed = average_speed

    def get_max_distance(self):
        """Calculate and return the maximum distance the electric scooter can travel on a battery charge. """
        return self.__time_to_drive_on_battery_charge * self.__average_speed

    @property
    def time_to_drive_on_battery_charge(self):
        """ Get the time the electric scooter can drive on a battery charge."""
        return self.__time_to_drive_on_battery_charge

    @property
    def average_speed(self):
        """ Get the average speed of the electric scooter."""
        return self.__average_speed

    def __str__(self):
        """Return a string representation of the ElectricScooter object."""
        return f"ElectricScooter: type={self.type_of_bicycle}, brand={self.brand}, " \
               f"max_speed={self.max_speed}, current_speed={self.current_speed}, " \
               f"time_to_drive_on_battery_charge={self.time_to_drive_on_battery_charge}, " \
               f"average_speed={self.average_speed}"

from manager.bicycle_manager import BicycleManager
from models.abstract_bicycle import AbstractBicycle
from models.bicycle import Bicycle
from models.electric_bicycle import ElectricBicycle
from models.electric_scooter import ElectricScooter
from models.gyro_scooter import GyroScooter
from exceptions.bicycle_brake_exception import BicycleBrakeException

def main():
    bicycle_manager = BicycleManager()
    bicycle1 = Bicycle("road", "Colnago", 60, 45, {"fast", "comfortable"})
    bicycle2 = Bicycle("mountain", "Trek", 55, 38, {"not expensive", "safe"})
    electric_bicycle1 = ElectricBicycle("road", "Colnago", 60, 40, 35, 0.2, {"unique", "qualitative"})
    electric_bicycle2 = ElectricBicycle("road", "Giant", 70, 30, 45, 0.6, {"ecological", "efficient"})
    electric_scooter1 = ElectricScooter("road", "Bolt", 30, 15, 2, 15, {"economical", "lightweight"})
    electric_scooter2 = ElectricScooter("road", "Bolt", 40, 12, 3, 17, {"agile", "stylish"})
    gyro_scooter1 = GyroScooter("mountain", "Smart Balance", 30, 10, 20, 36, 0.2, {"maneuverable", "self-balancing"})
    gyro_scooter2 = GyroScooter("road", "Smart Balance", 50, 20, 30, 48, 0.5, {"innovative", "compact)"})

    bicycle_manager.add_bicycles(bicycle1)
    bicycle_manager.add_bicycles(bicycle2)
    bicycle_manager.add_bicycles(electric_bicycle1)
    bicycle_manager.add_bicycles(electric_bicycle2)
    bicycle_manager.add_bicycles(electric_scooter1)
    bicycle_manager.add_bicycles(electric_scooter2)
    bicycle_manager.add_bicycles(gyro_scooter2)
    bicycle_manager.add_bicycles(gyro_scooter1)

    print(bicycle_manager.zip_return())
    for bicycle in bicycle_manager.bicycles:
        attributes = AbstractBicycle.get_attributes_by_type(bicycle, int)
        print(attributes)

    def condition(some_bicycle):
        return isinstance(some_bicycle, ElectricBicycle)

    print(bicycle_manager.all_and_any(condition))
    print(bicycle_manager.result_of_get_max_distance())
    print(bicycle_manager.enumerate_objects())

    bicycle1.brake(0)


if __name__ == "__main__":
    main()

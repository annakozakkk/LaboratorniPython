from manager.bicycle_manager import BicycleManager
from models.bicycle import Bicycle
from models.electric_bicycle import ElectricBicycle
from models.electric_scooter import ElectricScooter
from models.gyro_scooter import GyroScooter


def main():

    bicycle_manager = BicycleManager()

    bicycle1 = Bicycle("road", "Colnago", 60, 45)
    bicycle2 = Bicycle("mountain", "Trek", 55, 38)
    electric_bicycle1 = ElectricBicycle("road", "Colnago", 60, 40, 35, 0.2)
    electric_bicycle2 = ElectricBicycle("road", "Giant", 70, 30, 45, 0.6)
    electric_scooter1 = ElectricScooter("road", "Bolt", 30, 15, 2, 15)
    electric_scooter2 = ElectricScooter("road", "Bolt", 40, 12, 3, 17)
    gyro_scooter1 = GyroScooter("mountain", "Smart Balance", 30, 10, 20, 36, 0.2)
    gyro_scooter2 = GyroScooter("road", "Smart Balance", 50, 20, 30, 48, 0.5)

    bicycle_manager.add_bicycles(bicycle1)
    bicycle_manager.add_bicycles(bicycle2)
    bicycle_manager.add_bicycles(electric_bicycle1)
    bicycle_manager.add_bicycles(electric_bicycle2)
    bicycle_manager.add_bicycles(electric_scooter1)
    bicycle_manager.add_bicycles(electric_scooter2)
    bicycle_manager.add_bicycles(gyro_scooter2)
    bicycle_manager.add_bicycles(gyro_scooter1)

    for bicycle in bicycle_manager.bicycles:
        print(bicycle)
    print("\n")
    bicycles_speed_more_than = bicycle_manager.find_bicycles_with_max_speed_more_than(50)
    bicycles_with_brand = bicycle_manager.find_bicycles_by_brand("Smart Balance")
    print("Bicycles with max speed more than 50 : ")
    for bicycle in bicycles_speed_more_than:
        print(bicycle)
    print("\n")
    print("Bicycles with brand \"Smart Balance\" : ")
    for bicycle in bicycles_with_brand:
        print(bicycle)


if __name__ == "__main__":
    main()

class Bicycle:
    _type = ""
    _brand = ""
    _max_speed = 0
    _current_speed = 0

    def __init__(self, type="None", brand="None", max_speed=0, current_speed=0):
        self._type = type
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = current_speed

    @staticmethod
    def get_instance():
        Bicycle.instance = Bicycle("road", "Colnago", 40, 12)
        return Bicycle.instance

    def accelerate(self, speed):
        if speed < self._max_speed:
            self._current_speed += speed
            return self._current_speed
        else:
            return self._max_speed

    def brake(self):
        self._current_speed = 0
        return self._current_speed

    def slow_down(self, speed):
        if speed <= self._current_speed:
            self._current_speed -= speed
            return self._current_speed
        return self.brake()

    def __str__(self):
        return f"Bicycle: type={self._type}, brand={self._brand}, maxSpeed={self._max_speed}, currentSpeed={self._current_speed}"


bicycles = [Bicycle("road", "Trek", 40, 23), Bicycle(), Bicycle.get_instance(), Bicycle.get_instance()]

for bicycle in bicycles:
    print(bicycle)

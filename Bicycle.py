class Bicycle:
    type = ""
    brand = ""
    maxSpeed = 0
    currentSpeed = 0

    def __init__(self, type="None", brand="None", maxSpeed=0, currentSpeed=0):
        self.type = type
        self.brand = brand
        self.maxSpeed = maxSpeed
        self.currentSpeed = currentSpeed

    @classmethod
    def get_instance(cls):
        return cls("mountain", "Trek", 50, 30)

    def accelerate(self, speed):
        if speed < self.maxSpeed:
            self.currentSpeed += speed
            return self.currentSpeed
        else:
            return self.maxSpeed

    def brake(self):
        self.currentSpeed = 0
        return self.currentSpeed

    def slowDown(self, speed):
        if speed <= self.currentSpeed:
            self.currentSpeed -= speed
            return self.currentSpeed
        return self.brake()

    def __str__(self):
        return f"Bicycle: type={self.type}, brand={self.brand}, maxSpeed={self.maxSpeed}, currentSpeed={self.currentSpeed}"


bicycles = []
bicycles.append(Bicycle("road", "Trek", 40, 23))
bicycles.append(Bicycle())
bicycles.append(Bicycle.get_instance())
bicycles.append(Bicycle.get_instance())

for bicycle in bicycles:
    print(bicycle)

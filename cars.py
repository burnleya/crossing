from car import MyCars


class Cars:
    def __init__(self):
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for _ in range(9):
            new_car = MyCars()
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(2.5)


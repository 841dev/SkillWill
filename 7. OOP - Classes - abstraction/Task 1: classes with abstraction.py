from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, max_speed: int, current_speed: int):
        self.max_speed = max_speed
        self.current_speed = current_speed


    def start_engine(self):
        return "car started"


    def stop_engine(self):
        return "car stoped"

class SportCar(Car):
    def start_engine(self):
        return super().start_engine() + f", max speed: {self.max_speed} kmh"

    def stop_engine(self):
        self.current_speed = 0
        return super().stop_engine() + f", current speed {self.current_speed} kmh"



sport_car = SportCar(max_speed=180, current_speed=60)

print(sport_car.start_engine())
print(sport_car.stop_engine())

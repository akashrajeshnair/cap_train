import pytest
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start():
        pass

class Bike(Vehicle):
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"Bike {self.name} is starting." 
    
class Car(Vehicle):
    def __init__(self, name):
        self.name = name

    def start(self):
        return f"Car {self.name} is starting."
    
b = Bike('Pulsar')
c = Car('Verna')

def test_bike_start():
    assert b.start() == f"Bike {b.name} is starting."

def test_car_start():
    assert c.start() == f"Car {c.name} is starting."


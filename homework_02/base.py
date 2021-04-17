from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        necessary_fuel = distance / 100 * self.fuel_consumption
        if necessary_fuel <= self.fuel:
            self.fuel -= necessary_fuel
        else:
            raise exceptions.NotEnoughFuel

"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo: float
    max_cargo: float

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, cargo: float):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo

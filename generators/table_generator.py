from random import randint
from generators.random_generator import RandomDataGenerator
from abc import ABC, abstractmethod


class TableParameterGenerator(ABC):
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

        self.random_generator = RandomDataGenerator()
        self.supported_list = self.random_generator.supported_data

    @abstractmethod
    def generate_table(self):
        pass

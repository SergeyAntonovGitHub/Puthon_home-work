from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Jacket(Clothes):
    @property
    def consumption(self):
        return (2 * self.param + 0.3) / 100


coat = Coat(58)
jacket = Jacket(240)
print(coat + jacket)
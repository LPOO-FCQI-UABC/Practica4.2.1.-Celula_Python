# -*- coding: UTF-8 -*-
from Animal import Animal
from Organism import Organism

class Mammal(Animal):
    def grow(self):
        pass
    def eat (self):
        pass
    def __init__(self, aName, aColor, aSize,aCell,aSpecies, aSex):
        Animal.__init__(self,aName, aColor, aSize, aCell, aSpecies, aSex)
    def to_string(self):
        return super().to_string()
from Mammal import Mammal
from MarineAnimal import MarineAnimal

class Cetaceo(Mammal, MarineAnimal):
    def setType(self, aType):
        self.___type = aType
    def getType(self):
        return self.___type
    def grow(self):
        return "Cetaceo growing"
    def eat (self):
        return "Cetaceo eating"
    def __init__(self, aName, aColor, aSize,aCell,aSpecies, aSex, numOfFins, aType):
        Mammal.__init__(self,aName, aColor, aSize, aCell, aSpecies, aSex)
        MarineAnimal.__init__(self,aName, aColor, aSize, aCell, aSpecies, aSex, numOfFins)
        self.___type = aType
        """@AttributeType String"""
    def to_string(self):
        return "Cetaceo=[\nType: "+self.getType() + " " +MarineAnimal.to_string(self)+self.grow()+self.eat()+"]"
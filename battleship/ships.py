from enum import Enum
from typing import List, Tuple
from .coordinates import Coordinate

class ShipType(Enum):
    CARRIER = "Carrier"
    BATTLESHIP = "Battleship"
    CRUISER = "Cruiser"
    SUBMARINE = "Submarine"
    DESTROYER = "Destroyer"

class Ship():
    def __init__(self, ship_type:ShipType):
        self.length = 0
        self.ship_type: ShipType = ship_type
        self.ship_coordinates: List[Coordinate]  = []



    def __str__(self):
        return "Ship(ship_type={}, length={}, coordinates={})".format(self.ship_type.value, self.length, self.ship_coordinates)
    
class Carrier(Ship):
    def __init__(self):
        super().__init__(ShipType.CARRIER)
        self.length = 5


class Battleship(Ship):
    def __init__(self):
        super().__init__(ShipType.BATTLESHIP)
        self.length = 4


class Cruiser(Ship):
    def __init__(self):
        super().__init__(ShipType.CRUISER)
        self.length = 3


class Submarine(Ship):
    def __init__(self):
        super().__init__(ShipType.SUBMARINE)
        self.length = 3

class Destroyer(Ship):
    def __init__(self):
        super().__init__(ShipType.DESTROYER)
        self.length = 2

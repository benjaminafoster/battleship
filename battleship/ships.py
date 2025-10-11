import math
from enum import Enum
from typing import List, Tuple
from .coordinates import is_valid_coordinate, get_coordinate_distance
from .errors import CoordinateError

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
        self.ship_coordinates: List[Tuple[str,int]]  = []

    def position_ship(self, bow_coord: Tuple[str,int], stern_coord: Tuple[str,int]):
        bc_valid = is_valid_coordinate(bow_coord)
        sc_valid = is_valid_coordinate(stern_coord)

        if not bc_valid:
            raise CoordinateError(f"Invalid bow coordinate: {bow_coord}")
        
        if not sc_valid:
            raise CoordinateError(f"Invalid stern coordinate: {stern_coord}")

        distance_between_coordinates = get_coordinate_distance(bow_coord, stern_coord)

        if distance_between_coordinates != float(self.length) - 1:
            raise Exception(f"Coordinates and ship length mismatch; coordinates must span {self.length} units for a {self.ship_type.value}")
        
        self.ship_coordinates = [bow_coord, stern_coord]

    def __str__(self):
        return f"Ship Type: {self.ship_type.value}\nShip Length: {self.length}\nShip Coordinates: {self.ship_coordinates}"
    
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

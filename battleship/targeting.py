from enum import Enum
from typing import Tuple
from .board import Board, CoordinateStatus, ShipsBoard, TargetingBoard
from .coordinates import Coordinate

def commit_shot(targeting: TargetingBoard, opponent: ShipsBoard, coordinate: Coordinate) -> CoordinateStatus:

    try:
        coord_status = opponent.get_coord_status(coordinate)
    except Exception as e:
        raise Exception(f"Unknown error: {e}")

    if coord_status == CoordinateStatus.EMPTY:
        opponent.coordinates[coordinate.alpha][coordinate.num] = CoordinateStatus.MISS
        targeting.coordinates[coordinate.alpha][coordinate.num] = CoordinateStatus.MISS
        return CoordinateStatus.MISS
    elif coord_status == CoordinateStatus.OCCUPIED:
        opponent.coordinates[coordinate.alpha][coordinate.num] = CoordinateStatus.HIT
        targeting.coordinates[coordinate.alpha][coordinate.num] = CoordinateStatus.HIT
        return CoordinateStatus.HIT
    else:
        raise CoordAlreadyGuessedError(coordinate)
    

class CoordAlreadyGuessedError(Exception):
    def __init__(self, coordinate: Coordinate, message = "Coordinate already guessed"):
        self.message = "{}: {}".format(message, str(coordinate))
        super().__init__(self.message)


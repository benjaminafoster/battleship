from enum import Enum
from typing import Tuple
from .board import Board, CoordinateStatus
from .coordinates import is_valid_coordinate
from .errors import CoordAlreadyGuessedError

def commit_shot(target_board: Board, coordinate: Tuple[str, int]) -> CoordinateStatus:
    is_valid = is_valid_coordinate(coordinate)

    if not is_valid:
        raise ValueError(f"{coordinate} is not a vaild coordinate")
    
    alpha_val = coordinate[0]
    num_val = coordinate[1]

    try:
        coord_status = target_board.coordinates[alpha_val][num_val]
    except Exception as e:
        raise Exception(f"Unknown error: {e}")

    if coord_status == CoordinateStatus.EMPTY:
        target_board.coordinates[alpha_val][num_val] = CoordinateStatus.MISS
        return CoordinateStatus.MISS
    elif coord_status == CoordinateStatus.OCCUPIED:
        target_board.coordinates[alpha_val][num_val] = CoordinateStatus.HIT
        return CoordinateStatus.HIT
    else:
        raise CoordAlreadyGuessedError()


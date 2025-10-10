from enum import Enum
from typing import Tuple
from .board import Board, CoordinateStatus

class StrikeResult(Enum):
    HIT = "X"
    MISS = "O"

def commit_shot(board: Board, coordinate: Tuple[str, int]) -> StrikeResult:
    return StrikeResult.HIT # temp placeholder
from enum import Enum
from typing import List, Tuple
from .player import Player
from .coordinates import Coordinate

class BoardType(Enum):
    FRIENDLY = "Friendly"
    ENEMY = "Enemy"

class CoordinateStatus(Enum):
    EMPTY = "~"
    OCCUPIED = "^"
    MISS = "O"
    HIT = "X"

class Board:
    def __init__(self, board_type: BoardType, player: Player):
        self.player = player
        self.board_type = board_type
        self.coordinates = {
            'A': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'B': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'C': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'D': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'E': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'F': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'G': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'H': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'I': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            },
            'J': {
                0: CoordinateStatus.EMPTY,
                1: CoordinateStatus.EMPTY,
                2: CoordinateStatus.EMPTY,
                3: CoordinateStatus.EMPTY,
                4: CoordinateStatus.EMPTY,
                5: CoordinateStatus.EMPTY,
                6: CoordinateStatus.EMPTY,
                7: CoordinateStatus.EMPTY,
                8: CoordinateStatus.EMPTY,
                9: CoordinateStatus.EMPTY
            }
        }
    
    def place_ship(self, bow_coord: Coordinate, stern_coord: Coordinate):
        pass

    def get_board_availability(self, coord_list: List[Tuple[str, int]]) -> bool:
        for coord in coord_list:
            # check status of coordinate
            coord_status = self.coordinates[coord[0]][coord[1]]
            if coord_status == CoordinateStatus.OCCUPIED:
                return False
        
        return True

    def __str__(self):
        return f"{self.board_type.value} board for {self.player.player_name}"

class FriendlyBoard(Board):
    def __init__(self, player: Player):
        super().__init__(BoardType.FRIENDLY, player)

class EnemyBoard(Board):
    def __init__(self, player: Player):
        super().__init__(BoardType.ENEMY, player)
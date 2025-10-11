from enum import Enum

class BoardType(Enum):
    FRIENDLY = "friendly"
    ENEMY = "enemy"

class CoordinateStatus(Enum):
    EMPTY = "~"
    OCCUPIED = "^"
    MISS = "O"
    HIT = "X"

class Board:
    def __init__(self, board_type: BoardType):
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

class FriendlyBoard(Board):
    def __init__(self):
        super().__init__(BoardType.FRIENDLY)

class EnemyBoard(Board):
    def __init__(self):
        super().__init__(BoardType.ENEMY)
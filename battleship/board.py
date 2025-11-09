from enum import Enum
from typing import List, Tuple
from .player import Player
from .ships import Ship
from .coordinates import Coordinate, get_coordinate_distance

class BoardType(Enum):
    FRIENDLY = "Friendly"
    ENEMY = "Enemy"


class CoordinateStatus(Enum):
    EMPTY = "~"
    OCCUPIED = "^"
    MISS = "O"
    HIT = "X"


class ShipPlacementError(Exception):
    def __init__(self, ship: Ship, message="Ship placement error"):
        self.ship = ship
        self.message = "{}: {}".format(message, str(self.ship))
        super().__init__(self.message)


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
    
    def place_ship(self, ship: Ship, b_coord: Coordinate, s_coord: Coordinate):
        coord_distance = get_coordinate_distance(b_coord, s_coord)

        # check that coordinate distance equals ship length
        if ship.length != coord_distance + 1:
            raise ShipPlacementError(ship, "Ship length ({}) != Coord distance ({})".format(float(ship.length), coord_distance + 1))

        # get full list of coordinates between bow and stern
        temp_coord_list: List[Coordinate] = []
        if b_coord.alpha == s_coord.alpha:
            num_min = min(b_coord.num, s_coord.num)
            num_max = max(b_coord.num, s_coord.num)
            for i in range(num_min, num_max + 1):
                temp_coord_list.append(Coordinate(b_coord.alpha, i))
        elif b_coord.num == s_coord.num:
            alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
            b_alpha_index = alpha_list.index(b_coord.alpha)
            s_alpha_index = alpha_list.index(s_coord.alpha)
            alpha_min = min(b_alpha_index, s_alpha_index)
            alpha_max = max(b_alpha_index, s_alpha_index)
            for i in range(alpha_min, alpha_max + 1):
                temp_coord_list.append(Coordinate(alpha_list[i], b_coord.num))

        # check board availability for each coordinate

        # register all coordinates as OCCUPIED on board

    def get_coord_availability(self, coord: Coordinate) -> bool:
        coord_status = self.coordinates[coord.alpha][coord.num]
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
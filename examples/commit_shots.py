from battleship.coordinates import Coordinate
from battleship.ships import Cruiser, Carrier
from battleship.player import Player
from battleship.board import ShipsBoard, TargetingBoard, CoordinateStatus
from battleship.targeting import commit_shot

# create two players
player_1 = Player("Player 1")
ships_1 = ShipsBoard(player_1)
targeting_1 = TargetingBoard(player_1)

player_2 = Player("Player 2")
ships_2 = ShipsBoard(player_2)
targeting_2 = TargetingBoard(player_2)

# create example player 1 ship
cruiser = Cruiser()

bow_coord = Coordinate('a', 3)
stern_coord = Coordinate('a', 5)

ships_1.place_ship(cruiser, bow_coord, stern_coord)

ships_1.render_board()


# create example player 2 ship
carrier = Carrier()

carrier_bow = Coordinate('a', 8)
carrier_stern = Coordinate('e', 8)

ships_2.place_ship(carrier, carrier_bow, carrier_stern)
ships_2.render_board()

# commit 3 shots to yield the three possible outcomes (HIT, MISS, or already guessed)
coord_list = [Coordinate('b', 8), Coordinate('c', 2), Coordinate('b', 8)]

for coordinate in coord_list:
    try:
        result = commit_shot(targeting_1, ships_2, coordinate)
        if result == CoordinateStatus.HIT:
            print("HIT!!!")
        elif result == CoordinateStatus.MISS:
            print("MISS...")
    except Exception as e:
        print(e)


# render an example targeting board and ships board to show results
targeting_1.render_board()
ships_2.render_board()
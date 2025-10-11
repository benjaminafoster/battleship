from battleship.ships import Carrier, Battleship, Cruiser, Submarine, Destroyer
from battleship.board import FriendlyBoard
from battleship.targeting import commit_shot

dummy_board = FriendlyBoard()

carrier = Carrier()
bow_coord = ("A", 1)
stern_coord = ("E", 1)

battleship = Battleship()
bb_coord = ("A", 2)
bs_coord = ("D", 2)

cruiser = Cruiser()
cb_coord = ("A", 3)
cs_coord = ("C", 3)

submarine = Submarine()
sb_coord = ("A", 4)
ss_coord = ("C", 4)

destroyer = Destroyer()
db_coord = ("A", 5)
ds_coord = ("B", 5)


carrier.position_ship(dummy_board, bow_coord, stern_coord)
battleship.position_ship(dummy_board, bb_coord, bs_coord)
cruiser.position_ship(dummy_board, cb_coord, cs_coord)
submarine.position_ship(dummy_board, sb_coord, ss_coord)
destroyer.position_ship(dummy_board, db_coord, ds_coord)

print(carrier)
print(battleship)
print(cruiser)
print(submarine)
print(destroyer)
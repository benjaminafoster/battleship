from battleship.ships import Carrier, Battleship, Cruiser, Submarine, Destroyer
from battleship.board import FriendlyBoard
from battleship.targeting import commit_shot

""" carrier = Carrier()
bow_coord = ("A", 1)
stern_coord = ("A", 5)
destroyer = Destroyer()
db_coord = ("E", 4)
ds_coord = ("F", 4)


carrier.position_ship(bow_coord, stern_coord)
destroyer.position_ship(db_coord, ds_coord)

print(carrier)
print(destroyer) """

board = FriendlyBoard()
coord = ("A", 4)

print(board.coordinates["A"])
commit_shot(board, coord)
print(board.coordinates["A"])
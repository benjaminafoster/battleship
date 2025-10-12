import unittest
from battleship.ships import Carrier, Battleship, Cruiser, Submarine, Destroyer
from battleship.board import FriendlyBoard

class ShipsTest(unittest.TestCase):
    def test_correct_definitions(self):
        test_data = [
            (Carrier().__str__(), "Ship Type: Carrier\nShip Length: 5\nShip Coordinates: []\n"),
            (Battleship().__str__(), "Ship Type: Battleship\nShip Length: 4\nShip Coordinates: []\n"),
            (Cruiser().__str__(), "Ship Type: Cruiser\nShip Length: 3\nShip Coordinates: []\n"),
            (Submarine().__str__(), "Ship Type: Submarine\nShip Length: 3\nShip Coordinates: []\n"),
            (Destroyer().__str__(), "Ship Type: Destroyer\nShip Length: 2\nShip Coordinates: []\n"),
        ]

        for case in test_data:
            self.assertEqual(case[0], case[1])

        

if __name__ == "__main__":
    unittest.main()
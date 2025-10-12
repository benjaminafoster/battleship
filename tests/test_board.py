import unittest
from battleship.board import Board, FriendlyBoard, EnemyBoard, CoordinateStatus, BoardType
from battleship.player import Player

class BoardTests(unittest.TestCase):
    def test_board_definition(self):
        test_player = Player("test")
        test_data = [
            (Board(BoardType.FRIENDLY, test_player).__str__(), "Friendly board for test"),
            (FriendlyBoard(test_player).__str__(), "Friendly board for test"),
            (EnemyBoard(test_player).__str__(), "Enemy board for test")
        ]

        for case in test_data:
            self.assertEqual(case[0], case[1], f"{case[0]} != {case[1]}")


    def test_coordinate_availability(self):
        test_player = Player("test")
        board = FriendlyBoard(test_player)
        occupied_coordinates = [("B", 2), ("B", 3), ("B", 4), ("B", 5)]
        for coord in occupied_coordinates:
            board.coordinates[coord[0]][coord[1]] = CoordinateStatus.OCCUPIED

        test_data = [
            ([("A", 1), ("A", 2), ("A", 3)], True),
            ([("A", 2), ("B", 2), ("C", 2)], False),
            ([("A", 5), ("B", 5), ("C", 5)], False),
            ([("B", 6), ("B", 7), ("B", 8)], True)
        ]

        for case in test_data:
            self.assertEqual(board.get_board_availability(case[0]), case[1], f"Case: {case[0]}")



if __name__ == "__main__":
    unittest.main()
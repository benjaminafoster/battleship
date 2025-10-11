import unittest
from battleship.coordinates import is_valid_coordinate, get_coordinate_distance

class CoordinateTests(unittest.TestCase):
    def test_valid_coordinate(self):
        test_data = [
            [("A", 0), True],
            [("A", 9), True],
            [("A", 10), False],
            [("A", -1), False],
            [("J", 0), True],
            [("J", 9), True],
            [("J", 10), False],
            [("J", -1), False],
            [("J", -50), False]
        ]

        for case in test_data:
            coord, expected = case[0], case[1]
            self.assertEqual(is_valid_coordinate(coord), expected) 
        
    def test_coordinate_distance(self):
        test_data = [
            [("A", 1), ("A", 5), 5], # [bow_coord, stern_coord, expected_distance]
            [("A", 1), ("E", 1), 5],
            (("A", 1), ("C", 2), 3.2361)
        ]

        for bow_coord, stern_coord, expected_distance in test_data:
            adjusted_distance = get_coordinate_distance(bow_coord, stern_coord) + 1.0
            self.assertEqual(round(adjusted_distance, 4), float(expected_distance))


if __name__ == '__main__':
    unittest.main()
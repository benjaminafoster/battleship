import math


class Coordinate:
    def __init__(self, alpha_coord: str, num_coord: int):
        self.alpha = alpha_coord.lower()
        self.num = num_coord

        self.validate_coordinate()

    def validate_coordinate(self):
        # Valid alpha coordinate options
        alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

        # Raise CoordinateErorr if alpha coordinate isn't in alpha_list
        if self.alpha not in alpha_list:
            raise CoordinateError(self)
        
        # Raise CoordinateError if number coordinate isn't 0<self.num<=9
        if not self.num > 0 or not self.num <= 9:
            raise CoordinateError(self)
        

        
    def __str__(self):
        return "Coordinate(alpha_coord={}, num_coord={})".format(self.alpha, self.num)


def get_coordinate_distance(bow_coord: Coordinate, stern_coord: Coordinate) -> float:
    # coordinates already validated; need to convert letter portion and find distance

    alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    bow_alpha_index = alpha_list.index(bow_coord.alpha)
    stern_alpha_index = alpha_list.index(stern_coord.alpha)
    
    # finding distance using Eucladian distance formula; must add one to returned distance to be end-point inclusive
    distance = math.dist((bow_alpha_index, bow_coord.num), (stern_alpha_index, stern_coord.num))

    return distance

class CoordinateError(Exception):
    def __init__(self, coord: Coordinate, message="Invalid coordinate provided"):
        self.coord = coord
        self.message = "{}: {}".format(message, str(coord))
        super().__init__(self.message)
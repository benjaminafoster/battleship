import math
from typing import Tuple

def is_valid_coordinate(coordinate: Tuple[str,int]) -> bool:
    alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    alpha_coord = coordinate[0]
    num_coord = coordinate[1]

    # check if first tuple value is a letter
    try:
        if not alpha_coord.isalpha():
            return False
    except AttributeError: # raised when 'int' type has no ".isalpha" method
        return False
    
    # check if the second tuple value is an integer
    try:
        if not num_coord.is_integer():
            return False
    except AttributeError: # rasied when 'str' type has no ".is_integer" method
        return False

    # check if first tuple value has an index value within the approved letters list
    try:
        alpha_list.index(alpha_coord.lower())
    except IndexError:
        return False
    except ValueError:
        return False

    # check if the second tuple value is an integer between 0 and 9
    if num_coord < 0 or num_coord > 9:
        return False

    return True

def get_coordinate_distance(bow_coord: Tuple[str, int], stern_coord: Tuple[str, int]) -> float:
    # coordinates already validated; need to convert letter portion and find distance

    alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    ba_coord, bn_coord = bow_coord[0], bow_coord[1]
    sa_coord, sn_coord = stern_coord[0], stern_coord[1]

    try:
        int_bow_alpha = alpha_list.index(ba_coord.lower())
        int_stern_alpha = alpha_list.index(sa_coord.lower())
    except IndexError:
        return False
    except ValueError:
        return False
    
    distance = math.dist((int_bow_alpha, bn_coord), (int_stern_alpha, sn_coord))

    return distance

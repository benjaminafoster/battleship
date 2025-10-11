class CoordinateError(Exception):
    def __init__(self, message="Invalid coordinate provided"):
        self.message = message
        super().__init__(self.message)

class CoordAlreadyGuessedError(Exception):
    def __init__(self, message="Coordinate already guessed"):
        self.message = message
        super().__init__(self.message)

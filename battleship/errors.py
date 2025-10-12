class CoordinateError(Exception):
    def __init__(self, message="Invalid coordinate provided"):
        self.message = message
        super().__init__(self.message)

class CoordAlreadyGuessedError(Exception):
    def __init__(self, message="Coordinate already guessed"):
        self.message = message
        super().__init__(self.message)

class CoordinateAvailabilityError(Exception):
    def __init__(self, message="One or more of the provided coordinates are already occupied on your board"):
        self.message = message
        super().__init__(self.message)

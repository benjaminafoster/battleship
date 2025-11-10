

class Player:
    def __init__(self, player_name: str):
        self.name = player_name
        self.player_score = 0

    def __str__(self):
        return f"Player name: {self.name}"
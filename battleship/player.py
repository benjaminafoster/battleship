class Player:
    def __init__(self, player_name: str):
        self.player_name = player_name

    def __str__(self):
        return f"Player name: {self.player_name}"
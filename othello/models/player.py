from enum import Enum

class Player(Enum):
    """Enumeration representing the players in the game.

    Members:
        BLACK: Represents the black player (0).
        WHITE: Represents the white player (1).

    Notes:
        The players are represented as binary units, with BLACK as 0 
        and WHITE as 1. This allows for easy comparisons and 
        representation in game logic.
    """
    BLACK = 0
    WHITE = 1
    
    def __eq__(self, other: object) -> bool:
        return self.value == other


def get_opponent(player: Player) -> Player:
    """Returns the opponent of the specified player.

    Args:
        player (Player): The player for whom to find the opponent.

    Returns:
        Player: The opponent of the given player; returns Player.BLACK 
        if the player is Player.WHITE, and Player.WHITE if the player 
        is Player.BLACK.
    """
    return Player.BLACK if player == Player.WHITE else Player.WHITE

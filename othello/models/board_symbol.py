from enum import Enum
from othello.models.player import Player

class BoardSymbol(Enum):
    """Enumeration representing symbols used on the game board.

    Members:
        WHITE: Symbol representing the white player (○).
        BLACK: Symbol representing the black player (●).
        EMPTY: Symbol indicating an empty space (□).
        LEGAL_MOVE: Symbol indicating a legal move position (■).

    This enumeration provides a clear visual representation of the 
    game board's state, making it easier to interpret during gameplay.
    """
    WHITE = "○"
    BLACK = "●"
    EMPTY = "□"
    LEGAL_MOVE = "■" 
    
    def __eq__(self, other: object) -> bool:
        return self.value == other

    def __add__(self, other: str) -> str:
        return self.value + other

    def __str__(self) -> str:
        return self.value

def get_symbol(player: Player) -> BoardSymbol:
    """Converts the specified player to their corresponding board symbol.

    Args:
        player (Player): The player whose symbol is to be determined.

    Returns:
        BoardSymbol: The board symbol associated with the player; 
        returns BoardSymbol.BLACK for the black player and 
        BoardSymbol.WHITE for the white player.
    """
    return BoardSymbol.BLACK if player == Player.BLACK else BoardSymbol.WHITE
from enum import Enum

class GameResult(Enum):
    """Enumeration representing the possible outcomes of a game.

    Members:
        WHITE_WINS: Indicates that the white player has won the game.
        BLACK_WINS: Indicates that the black player has won the game.
        DRAW: Indicates that the game has ended in a draw.
        NO_WINNER: Indicates that the game is still ongoing or no winner has been determined.

    The string representation of each member provides a descriptive message about the game outcome.
    """
    WHITE_WINS = "White wins!"
    BLACK_WINS = "Black wins!"
    DRAW = "DRAW!"
    NO_WINNER = ""
    
    def __str__(self) -> str:
        return self.value

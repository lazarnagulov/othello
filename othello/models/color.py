from enum import Enum
from othello.models.player import Player

class Color(Enum):
    """Enumeration representing the colors used in the game.

    Members:
        BLACK: Represents the color black.
        WHITE: Represents the color white.
        GRAY: Represents the color gray, typically used for neutral or inactive states.
    """
    BLACK = "black"
    WHITE = "white"
    GRAY = "gray"


def get_color(player: int) -> Color:
    """Converts a player identifier to the corresponding color.

    Args:
        player (int): The player identifier.

    Returns:
        Color: The color associated with the specified player identifier.
    """
    match player:
        case Player.BLACK.value: return Color.BLACK
        case Player.WHITE.value: return Color.WHITE
        case _: raise Exception("Unreachable...")
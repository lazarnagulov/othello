from othello.models.player import Player
import othello.util.matrix as Matrix

class Board:
    """
    Othello board class.

    The board is represented by two 64-bit binary numbers:
    - `occupied`: Indicates whether each position on the board is occupied (1 if occupied, 0 if not).
    - `color`: Represents the color of the tiles (1 for white, 0 for black).
    """

    SIZE: int = 8
    """
    Othello board size, which is 8.
    """
        
    def __init__(self) -> None:
        """
        Create board with starting tiles.         
        """
        self.occupied: int = 0
        self.color: int = 0
        
        self.set_tile((3,3), Player.WHITE)
        self.set_tile((3,4), Player.BLACK)
        self.set_tile((4,4), Player.WHITE)
        self.set_tile((4,3), Player.BLACK)

    
    def is_occupied(self, position: tuple[int, int]) -> bool:
        """
        Check if the specified position on the board is occupied.

        Args:
            position (tuple[int, int]): A tuple representing the position (row, column).

        Returns:
            bool: True if the position is occupied, False otherwise.
        """
        return bool((self.occupied & Matrix.DECODE_MATRIX[position[0]][position[1]]) >> (position[0] * 8 + position[1])) 

    def get_tile_color(self, position: tuple[int, int]) -> int:
        """
        Retrieve the color at the specified position.

        Args:
            position (tuple[int, int]): A tuple representing the position (row, column).

        Returns:
            int: The player in the specified position. Returns -1 if the position is empty.
        """
        if self.is_occupied(position):
            return (self.color & Matrix.DECODE_MATRIX[position[0]][position[1]]) >> (position[0] * 8 + position[1])
        return -1
        
    def replace_opponent(self, position: tuple[int, int]) -> None:
        """
        Reverse the tile at the specified position.

        If the position is empty, this method does nothing.

        Args:
            position (tuple[int, int]): A tuple representing the position (row, column).
        """
        self.color ^= Matrix.DECODE_MATRIX[position[0]][position[1]]
    
    def set_tile(self, position: tuple[int, int], player: Player) -> None:
        """
        Occupy the tile at the specified position.

        Args:
            position (tuple[int, int]): A tuple representing the position (row, column).
            player (Player): The player occupying the tile.
        """
        self.occupied |= Matrix.DECODE_MATRIX[position[0]][position[1]]
        if player == Player.WHITE:
            self.color |= Matrix.DECODE_MATRIX[position[0]][position[1]]    
            
    def deepcopy(self) -> 'Board':
        """
        Create a deep copy of the Board object.

        Returns:
            Board: A new instance of the Board that is a copy of the original.
        """
        new_board = Board()
        new_board.color = self.color
        new_board.occupied = self.occupied
        return new_board
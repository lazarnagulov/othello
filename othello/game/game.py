from typing import Optional
from othello.models.board import Board
from othello.models.game_result import GameResult
from othello.models.player import Player, get_opponent
import othello.util.matrix as Matrix

class Game:
    """Othello game static class. It stores all possible moves, current player and number of tiles for each player.
    """    
    legal_moves: dict[tuple[int, int], list[tuple[int, int]]] = {}
    current_player: Player = Player.BLACK
    black_tiles: int = 2
    white_tiles: int = 2
    
    @staticmethod
    def get_moves(board: Board, player: Player) -> dict[tuple[int, int], list[tuple[int, int]]]:
        """Gets all possible moves for the specified player.

        Args:
            board (Board): The current state of the game board.
            player (Player): The player for whom to find possible moves.

        Returns:
        
            dict[tuple[int, int], list[tuple[int, int]]]: A dictionary mapping each possible move (position) 
            to a list of opponent positions that can be captured or affected by that move.
        """
        moves: dict[tuple[int,int],list[tuple[int,int]]] = {}
        for x in range(Board.SIZE):
            for y in range(Board.SIZE):
                opponents: list[tuple[int, int]] = Game.__is_legal_move(board, player, (x,y))
                if opponents:
                    moves[(x,y)] = opponents

        return moves
        
    @staticmethod
    def has_ended(board: Board) -> bool:
        if len(Game.get_moves(board, Game.current_player)) == 0 and len(Game.get_moves(board, Player.WHITE)) == 0:
            return True
        
        return False
        
    @staticmethod
    def get_winner() -> GameResult:
        """Determines the winner of the game if it has concluded.

        Returns:
            
            GameResult: An enumeration representing the outcome of the game. 
            Possible values include:
                - GameResult.WHITE_WINS: The white player has won.
                - GameResult.BLACK_WINS: The black player has won.
                - GameResult.DRAW: The game ended in a draw.
                - GameResult.NO_WINNER: The game is still ongoing.
        """
        if Game.white_tiles > Game.black_tiles:
            return GameResult.WHITE_WINS
        elif Game.white_tiles < Game.black_tiles:
            return GameResult.BLACK_WINS
        elif Game.white_tiles == Game.black_tiles:
            return GameResult.DRAW
        return GameResult.NO_WINNER
    
    @staticmethod
    def play(board: Board, player: Player, position: tuple[int, int], legal_moves: Optional[dict[tuple[int, int], list[tuple[int, int]]]] = None, bot: bool = False) -> bool:
        """Executes a turn for the specified player at the given position.

        Args:
            board (Board): The current state of the game board.
            player (Player): The player making the move.
            position (tuple[int, int]): The coordinates of the position (row, column) where the player wants to play.
            legal_moves (Optional[dict[tuple[int, int], list[tuple[int, int]]]]): A dictionary of legal moves available 
                for the player. Defaults to None, which uses the game's legal moves.
            bot (bool): Indicates whether the method is called by a bot. Defaults to False.

        Returns:
            bool: True if the move was successfully executed; False if the move is not possible.
        """
        if not legal_moves:
            legal_moves = Game.legal_moves
        if position not in legal_moves:
            print("Cannot make that move!")
            return False
        
        board.set_tile(position, player)
        for opponent in legal_moves[position]:
            board.replace_opponent(opponent)
        
        if not bot:
            if player == Player.BLACK:
                Game.black_tiles += 1 + len(legal_moves[position])
                Game.white_tiles -= len(legal_moves[position])
            else:
                Game.black_tiles -= len(legal_moves[position])
                Game.white_tiles += 1 + len(legal_moves[position])

        return True

    @staticmethod
    def get_board_score(board: Board, player: Player) -> float:
        """Calculates the score of the current board state for the specified player.

        Args:
            board (Board): The current state of the game board.
            player (Player): The player for whom the score is being calculated.

        Returns:
            float: The calculated score representing the player's advantage or disadvantage 
            based on the current board configuration. A higher score indicates a more favorable 
            position for the player.
        """
        opponent: Player = get_opponent(player)
        player_tiles: int = 0
        opponent_tiles: int = 0
        my_front_tiles: int = 0
        opp_front_tiles: int = 0
        p: float = 0
        c: float = 0
        l: float = 0
        m: float = 0
        f: float = 0
        d: float = 0

        for i in range(Board.SIZE):
            for j in range(Board.SIZE):
                if board.get_tile_color((i,j)) == player:
                    d += Matrix.HEURISTIC_MATRIX[i][j]
                    player_tiles += 1
                elif board.get_tile_color((i,j)) == opponent:
                    d -= Matrix.HEURISTIC_MATRIX[i][j]
                    opponent_tiles += 1
                if board.is_occupied((i,j)):
                    for direction in Matrix.DIRECTIONS:
                        x = i + direction[0]
                        y = j + direction[1]
                        if x >= 0 and x < 8 and y >= 0 and y < 8 and not board.is_occupied((x,y)):
                            if board.get_tile_color((i, j)) == player:
                                my_front_tiles += 1
                            elif board.get_tile_color((i,j)) == opponent:
                                opp_front_tiles += 1
                            break
                        
        if player_tiles > opponent_tiles:
            p = (100.0 * player_tiles) / (player_tiles + opponent_tiles)
        elif player_tiles < opponent_tiles:
            p = -(100.0 * opponent_tiles) / (player_tiles + opponent_tiles)
        else:
            p = 0

        if my_front_tiles > opp_front_tiles:
            f = -(100.0 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
        elif my_front_tiles < opp_front_tiles:
            f = (100.0 * opp_front_tiles) / (my_front_tiles + opp_front_tiles)
        else:
            f = 0
            
        player_tiles = 0
        opponent_tiles = 0

        if board.get_tile_color((0,0)) == player:
            player_tiles += 1
        elif board.get_tile_color((0,0)) == opponent:
            opponent_tiles += 1

        if board.get_tile_color((0,7)) == player:
            player_tiles += 1
        elif board.get_tile_color((0,7)) == opponent:
            opponent_tiles += 1

        if board.get_tile_color((7,0)) == player:
            player_tiles += 1
        elif board.get_tile_color((7,0)) == opponent:
            opponent_tiles += 1

        if board.get_tile_color((7,7)) == player:
            player_tiles += 1
        elif board.get_tile_color((7,7)) == opponent:
            opponent_tiles += 1
        c = 25 * (player_tiles - opponent_tiles)

        player_tiles = 0
        opponent_tiles = 0

        if not board.is_occupied((0, 0)):
            if board.get_tile_color((0, 1)) == player:
                player_tiles += 1
            elif board.get_tile_color((0, 1)) == opponent:
                opponent_tiles += 1

            if board.get_tile_color((1, 1)) == player:
                player_tiles += 1
            elif board.get_tile_color((1, 1)) == opponent:
                opponent_tiles += 1

            if board.get_tile_color((1, 0)) == player:
                player_tiles += 1
            elif board.get_tile_color((1, 0)) == opponent:
                opponent_tiles += 1

        if not board.is_occupied((0, 7)):
            if board.get_tile_color((0, 6)) == player:
                player_tiles += 1
            elif board.get_tile_color((0, 6)) == opponent:
                opponent_tiles += 1

            if board.get_tile_color((1, 6)) == player:
                player_tiles += 1
            elif board.get_tile_color((1, 6)) == opponent:
                opponent_tiles += 1

            if board.get_tile_color((1, 7)) == player:
                player_tiles += 1
            elif board.get_tile_color((1, 7)) == opponent:
                opponent_tiles += 1

        if not board.is_occupied((7, 0)):
            if board.get_tile_color((7, 1)) == player:
                player_tiles += 1
            elif board.get_tile_color((7, 1)) == opponent:
                opponent_tiles += 1

            if board.get_tile_color((6, 1)) == player:
                player_tiles += 1
            elif board.get_tile_color((6, 1)) == opponent:
                opponent_tiles += 1

            if board.get_tile_color((6, 0)) == player:
                player_tiles += 1
            elif board.get_tile_color((6, 0)) == opponent:
                opponent_tiles += 1

        if not board.is_occupied((7, 7)):
            if board.get_tile_color((6, 7)) == player:
                player_tiles += 1
            elif board.get_tile_color((6, 7)) == opponent:
                opponent_tiles += 1

            if board.get_tile_color((6, 6)) == player:
                player_tiles += 1
            elif board.get_tile_color((6, 6)) == opponent:
                opponent_tiles += 1

            if board.get_tile_color((7, 6)) == player:
                player_tiles += 1
            elif board.get_tile_color((7, 6)) == opponent:
                opponent_tiles += 1

        l = -12.5 * (player_tiles - opponent_tiles)
        
        player_tiles = len(Game.get_moves(board, player))
        opponent_tiles = len(Game.get_moves(board, opponent))

        if player_tiles > opponent_tiles:
            m = (100.0 * player_tiles) / (player_tiles + opponent_tiles)
        elif player_tiles < opponent_tiles:
            m = -(100.0 * opponent_tiles) / (player_tiles + opponent_tiles)
        else:
            m = 0

        score = (10 * p) + (801.724 * c) + (382.026 * l) + (78.922 * m) + (74.396 * f) + (10 * d)
        return score

    @staticmethod
    def switch_player() -> None:
        """Switches current player.
        """
        Game.current_player = get_opponent(Game.current_player)
    
            
    @staticmethod
    def __is_inside_board(position: tuple[int, int]) -> bool:
        """Checks if the given position is within the boundaries of the board.

        Args:
            position (tuple[int, int]): The position to check, represented as (row, column).

        Returns:
            bool: True if the position is within the board's boundaries; 
                False if it is outside.
        """
        return (0 <= position[0] < Board.SIZE) and (0 <= position[1] < Board.SIZE)
    
    @staticmethod
    def __get_opponents_in_dir(board: Board, player: Player, position: tuple[int, int], direction: tuple[int, int]) -> list[tuple[int, int]]:
        """Retrieves all opponent pieces in the specified direction from a given position.

        Args:
            board (Board): The current state of the game board.
            player (Player): The player for whom the check is being performed.
            position (tuple[int, int]): The starting position (row, column) from which to check.
            direction (tuple[int, int]): The direction to check, represented as a vector (row_offset, column_offset) 
                                        from the Matrix.DIRECTIONS.

        Returns:
            list[tuple[int, int]]: A list of positions (row, column) of all opponent pieces found in the specified direction.
        """
        opponents: list[tuple[int, int]] = []
        current_position: tuple[int, int] = (position[0] + direction[0], position[1] + direction[1])
        opponent: Player = get_opponent(player)

        while Game.__is_inside_board(current_position) and board.is_occupied(current_position):
            if board.get_tile_color(current_position) == opponent:
                opponents += [current_position]
                current_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            else:
                return opponents
        
        return []

    
    @staticmethod
    def __get_opponents(board: Board, player: Player, position: tuple[int, int]) -> list[tuple[int, int]]:
        """Retrieves all opponent pieces adjacent to the specified position.

        Args:
            board (Board): The current state of the game board.
            player (Player): The player for whom the check is being performed.
            position (tuple[int, int]): The position (row, column) from which to check for opponents.

        Returns:
            list[tuple[int, int]]: A list of positions (row, column) of all opponent pieces adjacent 
            to the specified position.
        """
        opponents: list[tuple[int, int]] = []
        for direction in Matrix.DIRECTIONS:
            opps: list[tuple[int, int]] = Game.__get_opponents_in_dir(board, player, position, direction)    
            if not opps:
                continue
            opponents += opps
        return opponents        
    
    @staticmethod
    def __is_legal_move(board: Board, player: Player, position: tuple[int, int]) -> list[tuple[int, int]]:
        """Checks if a move to the specified position is legal for the given player.

        Args:
            board (Board): The current state of the game board.
            player (Player): The player attempting to make the move.
            position (tuple[int, int]): The target position (row, column) for the move.

        Returns:
            list[tuple[int, int]]: An empty list if the move is not legal; 
            otherwise, a list of positions (row, column) of all opponent pieces 
            that would be captured by the move.
        """
        if board.is_occupied(position):
            return []
        
        return Game.__get_opponents(board, player, position)

import time
from math import inf
from typing import Optional
from othello.models.board import Board
from othello.game.game import Game
from othello.models.player import Player, get_opponent

class Bot:
    
    bail = False
    transposition_table: dict[int, tuple[int, float, tuple]] = {}
    """
    A dictionary that stores previously evaluated game states to optimize performance through transposition.

    Key:
        - `hash(board)`: An integer hash value representing the current state of the game board.

    Value:
        A tuple containing:
            - `depth` (int): The search depth at which this state was evaluated.
            - `score` (float): The evaluated score of the board state.
            - `move` (Optional[Tuple[int, int]]): The best move associated with this state, or None if no move is available.

    This transposition table allows for efficient retrieval and reuse of previously evaluated states, enhancing the performance of the Minimax algorithm with alpha-beta pruning.
    """
    
    def __minimax(self, board: Board, depth: int, alpha: float, beta: float, maximizingPlayer: bool, player: Player, start_time: float) -> tuple[float, Optional[tuple]]:
        """
        Implements the Minimax algorithm with alpha-beta pruning for optimal decision-making in two-player games.

        Args:
            board (Board): The current state of the game board.
            depth (int): The maximum depth to search in the game tree.
            alpha (float): The best value that the maximizing player can guarantee at the current level or above.
            beta (float): The best value that the minimizing player can guarantee at the current level or above.
            maximizingPlayer (bool): Indicates whether the current player is the maximizing player.
            player (Player): The player for whom the move is being evaluated.
            start_time (float): The time when the search started, used for time-limiting the algorithm.

        Returns:
        
            Tuple[float, Optional[Tuple[int, int]]]: A tuple containing the evaluated score and the best move (as coordinates) found for the current player, 
            or None if no move is available.
        """
        if time.time() - start_time >= 3.0:
            Bot.bail = True
        board_hash: int = hash((board.color, board.occupied))
        transposition: Optional[tuple[int, float, tuple]] = Bot.transposition_table.get(board_hash)
        if transposition and transposition[0] >= depth:
            return transposition[1], transposition[2]

        moves: dict[tuple[int, int], list[tuple[int, int]]] = Game.get_moves(board, player)

        if depth == 0 or len(moves) == 0 or Bot.bail:
            score: float = Game.get_board_score(board, player)
            return score, None
        
        if maximizingPlayer:
            max_eval: float = -inf
            eval: float = -inf
            best_move: tuple = ()
            for move in moves:
                next_state: Board = board.deepcopy()
                Game.play(next_state, player, move, moves, True)
                eval, _ = self.__minimax(next_state, depth - 1, alpha, beta, False, get_opponent(player), start_time)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            Bot.transposition_table[board_hash] = (depth, max_eval, best_move)
            return max_eval, best_move
        else:
            min_eval = inf
            eval = inf
            best_move = ()
            for move in moves:
                next_state = board.deepcopy()
                Game.play(next_state, player, move, moves, True)
                eval, _ = self.__minimax(next_state, depth - 1, alpha, beta, True, get_opponent(player), start_time)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            Bot.transposition_table[board_hash] = (depth, min_eval, best_move)
            return min_eval, best_move        
    
    def bot_move(self, board: Board, time_limit: float = 3.0, depth_limit: int = 7) -> Optional[tuple[int, int]]:
        """Finds the best possible move using the Minimax algorithm with iterative deepening.

        Args:
            board (Board): The current state of the game board.
            time_limit (float, optional): The maximum time allowed for the search in seconds. Defaults to 3.0.
            depth_limit (int, optional): The maximum depth to search in the game tree. Defaults to 7.

        Returns:
            
            Optional[tuple[int, int]]: The coordinates of the best possible move found (row, column), 
            or None if no move is available.
        """
        best_score: float = -inf
        best_move: Optional[tuple] = ()
        depth: int = 1

        move_count: int = len(Game.get_moves(board, Player.WHITE))

        if move_count == 0:
            return None

        Bot.bail = False
        search_limit: float = (time_limit - 0.25) / move_count
        start_time: float = time.time()
        
        while time.time() - start_time < search_limit and depth <= depth_limit:
            score, move = self.__minimax(board, depth, -inf, inf, True, Player.WHITE, start_time)
            if score > best_score:
                best_score = score
                best_move = move
            if move_count == 1:
                break
            depth += 1            

        
        print(f"Time: {time.time() - start_time}")
        print(f"Depth: {min(depth, depth_limit)}")
        print(f"Move: {best_move}")
                
        return best_move
        
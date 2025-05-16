from typing import Optional
from othello.models.player import Player
from othello.models.board_symbol import BoardSymbol, get_symbol
from othello.models.game_result import GameResult
from othello.game.game import Game
from othello.game.bot import Bot
from othello.models.board import Board

from .user_interface import UserInterface

class ConsoleInterface(UserInterface):

    def __init__(self, argv: list[str]) -> None:
        self.bot_on: bool = True
        if len(argv) == 3:
            match argv[2]:
                case '--bot' | '-b': self.bot_on = True
                case '--player' | '-p': self.bot_on = False
                case _: self.bot_on = True
                
    def run(self) -> None:
      
        game_board: Board = Board()
        if self.bot_on:
            bot: Bot = Bot()    
    
        while True:
            Game.legal_moves = Game.get_moves(game_board, Game.current_player)
            print("=====================================================")
            self.display_current_player(Game.current_player)
            self.display_score(Game.white_tiles, Game.black_tiles)
            print("=====================================================")
            self.display_board(game_board, Game.legal_moves)
            if Game.has_ended(game_board):
                self.display_score(Game.white_tiles, Game.black_tiles)
                self.display_board(game_board, Game.legal_moves)
                self.display_result(Game.get_winner())
                break

            while True:
                try:
                    print("Please enter your move in the format: <row>,<column>")
                    print("For example: 3,5 (to place a piece at row 3, column 5)")
                    print("Type 'exit' to quit the program at any time.")
                    op: str = input(">> ")
                    if op == "exit":
                        return
                    x,y = op.split(",")

                    if Game.play(game_board, Game.current_player, (int(x),int(y))):
                        Game.switch_player()
                        self.display_score(Game.white_tiles, Game.black_tiles)
                        self.display_board(game_board, Game.legal_moves)
                        break  
                except:
                        print("Invalid input!")
                        continue
            if self.bot_on:
                bot_move: Optional[tuple[int, int]] = bot.bot_move(game_board)
                if bot_move:
                    Game.play(game_board, Game.current_player, bot_move, Game.get_moves(game_board, Player.WHITE))
                else:
                    self.display_result(Game.get_winner())
                    break
            
                Game.switch_player()            
    
    def display_current_player(board, current_player: Player) -> None:
        print(f"Current player: {get_symbol(current_player)}")
   
    def display_score(self, white_tiles: int, black_tiles: int) -> None:
        print(f"{get_symbol(Player.WHITE)}: {white_tiles} - {get_symbol(Player.BLACK)}: {black_tiles}")
        
    def display_board(self, board: Board, legal_moves: dict[tuple[int, int], list[tuple[int, int]]]) -> None:
        string_board: str = "# "
        for i in range(Board.SIZE):
            string_board += str(i) + " "
        string_board += "\n"
        for x in range(Board.SIZE):
            for y in range(Board.SIZE):
                if y == 0:
                    string_board += str(x) + " "
                occupied: int = board.is_occupied( (x,y))
                if occupied:
                    color: int = board.get_tile_color((x,y))
                    if color == Player.WHITE:
                        string_board += BoardSymbol.WHITE + " "
                    else:
                        string_board += BoardSymbol.BLACK + " "
                elif (x,y) in legal_moves:
                    string_board += BoardSymbol.LEGAL_MOVE + " "
                else:
                    string_board += BoardSymbol.EMPTY + " "
            string_board += "\n"

        print(string_board)
    
    def display_result(self, result: GameResult) -> None: 
        print(result)
        
         

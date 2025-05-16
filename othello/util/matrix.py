"""Matrix constants.
"""
DECODE_MATRIX: list[list[int]] = [
        [0x1, 0x2, 0x4, 0x8, 0x10, 0x20, 0x40, 0x80],
        [0x100, 0x200, 0x400, 0x800, 0x1000, 0x2000, 0x4000, 0x8000],
        [0x10000, 0x20000, 0x40000, 0x80000, 0x100000, 0x200000, 0x400000, 0x800000],
        [0x1000000, 0x2000000, 0x4000000, 0x8000000, 0x10000000, 0x20000000, 0x40000000, 0x80000000],
        [0x100000000, 0x200000000, 0x400000000, 0x800000000, 0x1000000000, 0x2000000000, 0x4000000000, 0x8000000000], 
        [0x10000000000, 0x20000000000, 0x40000000000, 0x80000000000, 0x100000000000, 0x200000000000, 0x400000000000, 0x800000000000], 
        [0x1000000000000, 0x2000000000000, 0x4000000000000, 0x8000000000000, 0x10000000000000, 0x20000000000000, 0x40000000000000, 0x80000000000000], 
        [0x100000000000000, 0x200000000000000, 0x400000000000000, 0x800000000000000, 0x1000000000000000, 0x2000000000000000, 0x4000000000000000, 0x8000000000000000]
    ]
"""
A matrix of bit masks used to decode the game board state.

Each entry in the matrix corresponds to a specific board position and represents 
a unique bitmask that can be used for efficient state encoding and decoding 
during game evaluations.
"""


HEURISTIC_MATRIX: list[list[int]] = [
        [20, -3, 11, 8, 8, 11, -3, 20],
        [-3, -7, -4, 1, 1, -4, -7, -3],
        [11, -4, 2, 2, 2, 2, -4, 11],
        [8, 1, 2, -3, -3, 2, 1, 8],
        [8, 1, 2, -3, -3, 2, 1, 8],
        [11, -4, 2, 2, 2, 2, -4, 11],
        [-3, -7, -4, 1, 1, -4, -7, -3],
        [20, -3, 11, 8, 8, 11, -3, 20]
    ]
"""
A matrix used to evaluate heuristics for the game.

This matrix contains heuristic values for different board positions, 
which helps the algorithm assess the desirability of each state during 
gameplay. The values are designed to guide the decision-making process 
in favor of optimal moves.
"""

DIRECTIONS: list[tuple[int,int]] = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
"""
A list of all possible directions represented in the matrix.

Each direction corresponds to a potential movement or action within the game, 
defined as vectors that indicate how to navigate the game board. This can 
include horizontal, vertical, and diagonal movements, facilitating 
move generation and evaluation during gameplay.
"""
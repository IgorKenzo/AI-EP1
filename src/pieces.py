from enum import Enum
import chess

class Pieces(Enum):
    pawn = chess.PAWN
    knight = chess.KNIGHT
    bishop = chess.BISHOP
    rook = chess.ROOK
    queen = chess.QUEEN
    king = chess.KING
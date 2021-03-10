import chess
from pieces import Pieces
import random


board = chess.Board()
legalMovesList = board.legal_moves
moves = []
while not board.is_game_over():
    moves.clear()
    for move in legalMovesList:
        moves.append(move)

    board.push(random.choice(moves))

print(board)
print(board.result())
print(board.is_fivefold_repetition())

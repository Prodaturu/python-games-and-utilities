import math
import random

class TicTacToe:
  def __init__(self):
    self.board = [' ' for _ in range(9)] # list to replicate 3*3 board
    self.current_winner = None # keeps track of winner

  def print_board(self):
    for row in [self.board[i*3]:[i+1]*3 for i in range(3)]:
      print('|' + '|'.join(row) + '|')
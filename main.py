from input import *
from display import *
from winning import *
import traceback
import os;

board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
ch = "X"
try:
  ch = getUser()
except ValueError as ve:
  print(ve)
i = 0
while i < 9:
  try:
    os.system('clear')
    displayBoard(board,ch)
    board = boardinput(board,ch)
    winner = getWinner(board)
    if (winner):
      displayBoard(board,ch)
      print("Congratulation Player", winner, "has won!!!")
      exit();
    ch = 'O' if ch == 'X' else 'X'
    i += 1
  except ValueError as ve:
    print(ve)
  except Exception as e:
    traceback.print_exc()
    print(e)
    exit()
print("Game Draw!!\nWell Played")

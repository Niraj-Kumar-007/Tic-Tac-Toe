#Input user's sign in the board
def getUser():
# num = int(input("Do you want to play with another user? Press 1 \n If not,Want to play with computer? Press 2 \n Want to exit game? Press 0 \n Enter Your Response:"))
  # if num > 2:
  #   raise ValueError("Error! Please input correct response")
  sign = input("Enter the sign you want play(Cross 'X' or Circle 'O'):")
  if sign.upper() != "X" or sign.upper() != 'O':
    raise ValueError("Error! Wrong Input (Please Provide 'X' or 'O')")
  return sign.upper()
# Input board's position in the game --------------------------------    
def boardinput(board,ch):
  
  x = int(input("Enter the board's position: "))
  if x < 1 or x > 9: 
    raise ValueError("Error! Please Try Again")
  x -= 1
  if board[x//3][x%3] != '_':
    raise ValueError("Error! Place Already Occupied!")
  board[x//3][x%3] = ch
  return board 
  
  

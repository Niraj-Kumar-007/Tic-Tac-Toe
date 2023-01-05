#Input user's sign in the board -------------------------------------
def getUser():
  sign = input("Enter the sign you want play(Cross 'X' or Circle 'O'):").upper()
  # print(sign)
  if sign != "X" and sign != 'O':
    raise ValueError("Error! Wrong Input (Please Provide 'X' or 'O')")
  return sign
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
  
  

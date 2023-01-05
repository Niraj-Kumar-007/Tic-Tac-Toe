def getWinner(board):
  winner="_"
  #horizontal----------------------------------------------
  # 1st
  if(board[0][1]== board[0][0] and board[0][1]==board[0][2]):
    winner= board[0][0];
  #2nd
  if(board[1][1]== board[1][0] and board[1][1]==board[1][2]):
    winner= board[1][0];
  #3rd
  if(board[2][1]== board[2][0] and board[2][1]==board[2][2]):
    winner= board[2][0];
  #vertical------------------------------------------------
  #1st
  if(board[1][0]== board[0][0] and board[1][0]==board[2][0]):
    winner= board[1][0];
  #2nd
  if(board[1][1]== board[0][1] and board[1][1]==board[2][1]):
    winner= board[1][1];
  #3rd
  if(board[1][2]== board[0][2] and board[1][2]==board[2][2]):
    winner= board[0][2];
  #diagonal------------------------------------------------
  if(board[1][1]== board[0][0] and board[1][1]==board[2][2]):
    winner= board[0][0];
  if(board[1][1]== board[0][2] and board[1][1]==board[2][0]):
    winner= board[0][2];
  if(winner=="_"):
    return None;
  else:
    return winner;
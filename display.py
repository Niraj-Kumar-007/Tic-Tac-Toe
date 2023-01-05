def displayBoard(board,ch):
  print(ch,"Player chance")
  print("----------------------------Your current board---------------------------")
  for i in board:
    for j in i:
      print(j,end=" ");
    print();
  print()
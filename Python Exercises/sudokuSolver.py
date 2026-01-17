""" Valid Sudoku Exercise:

   Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

      Each row must contain the digits 1-9 without repetition.

      Each column must contain the digits 1-9 without repetition.

      Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

   Note:
      A Sudoku board (partially filled) could be valid but is not necessarily solvable.

      Only the filled cells need to be validated according to the mentioned rules.

   Example 1:
      Input: board = 
                     [["5","3",".",".","7",".",".",".","."]
                     ,["6",".",".","1","9","5",".",".","."]
                     ,[".","9","8",".",".",".",".","6","."]
                     ,["8",".",".",".","6",".",".",".","3"]
                     ,["4",".",".","8",".","3",".",".","1"]
                     ,["7",".",".",".","2",".",".",".","6"]
                     ,[".","6",".",".",".",".","2","8","."]
                     ,[".",".",".","4","1","9",".",".","5"]
                     ,[".",".",".",".","8",".",".","7","9"]]
      Output: true

   Example 2:
      Input: board = 
                     [["8","3",".",".","7",".",".",".","."]
                     ,["6",".",".","1","9","5",".",".","."]
                     ,[".","9","8",".",".",".",".","6","."]
                     ,["8",".",".",".","6",".",".",".","3"]
                     ,["4",".",".","8",".","3",".",".","1"]
                     ,["7",".",".",".","2",".",".",".","6"]
                     ,[".","6",".",".",".",".","2","8","."]
                     ,[".",".",".","4","1","9",".",".","5"]
                     ,[".",".",".",".","8",".",".","7","9"]]
      Output: false
      
   Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
#Given an array containing 9 arrays of 9 ints from 1-9 as well as a "." if the space isn'f filled, we need to check that every element in said array is valid according to Sudoku's rules.

import pprint #want this to print out the sudoku boards in more readable format

import copy #need a way to create an entirely new copy of the game board which will be altered first to avoid overwriting the actual game board, and ".copy()" isn't good enough for a list of lists

def validityChecker(board: list[list[str]]) -> bool:
   
   #Going to create new empty list of 9 empty lists to store sub boxes for checking later
   subBox = [[], [], [], [], [], [], [], [], []]

   #need to check every single value inside each list which are inside the big list (called board) that the func was passed. Also need way to track which values are in which rows, collumns 
   #and 3x3 sub-boxes. Rows is already covered (currently each list inside board is a row), but collumns will need to be made I think, and definitely sub-boxes.

   #======================================================================== ROW and COL CHECK ==============================================================================================

   #Gets the list which represents each row of the board as row, i will function as index of rows inside board
   for i, row in enumerate(board): 
        
      #need to get every value inside of each row as val, j is index of vals inside each row
      for j, val in enumerate(row): 

         #CHECK IF VAL IS ACTUAL INT OR NOT, we don't need to check periods since they are considered empty spaces
         if (val != "."):

            #ROW CHECK val against every other value inside same row for duplicates ========================================================================================== ROW
            #so we use from val's j index+1 to end of the row, since once a val is checked and cleared at index j, we wont need to check the same index again
            for x in range(j+1, len(row)):
            
               if (val == row[x]):

                  print(f"\n Duplicate value in ROW, at row {i} and col {j}, where val = {val}, and row[{x}]: {row[x]}" )

                  return False

            #COL CHECK val against every other value inside same col for duplicates ========================================================================================== COL
            #so we use from val's i index+1 to end of the col, since once a val is checked and cleared at index i, we wont need to check the same index again
            for y in range(i+1, len(board)):
            
               if (val == board[y][j]):

                  print(f"\n Duplicate value in COL, at row {i} and col {j}, where val = {val}, and board[{y}][{j}]: {board[y][j]}" )

                  return False


            #SUB-BOX CREATE list of lists in order to check each sub-box for duplicates after ================================================================================ SUB-BOX
            #Following ifs place each val inside a new list made to represent the sub-box they are in on the board, so that we can check for duplicates, doesn't add ".", only ints

            if (i <=2): #if we r on row 0-2, we want to add to 0-2 ============================================== OUTER 0-2 ================================

               #if value is in first sub-box within the first 3 rows, add it to sub-box list 0
               if (j <=2):
                  subBox[0].append(val)

               #if value is in second sub-box within the first 3 rows, add it to sub-box list 1
               elif (j > 2 and j <= 5):
                  subBox[1].append(val)

               #if value is in third sub-box within the first 3 rows, add it to sub-box list 2
               elif (j > 5 and j <= 8):
                  subBox[2].append(val)

            elif (i > 2 and i <= 5): #if we r on row 3-5, we want to add to sub-box 3-5 ================ OUTER 3-5 ================================

               #if value is in first sub-box within rows 3-5, add it to sub-box list 3
               if (j <=2):
                  subBox[3].append(val)

               #if value is in second sub-box within rows 3-5, add it to sub-box list 4
               elif (j > 2 and j <= 5):
                  subBox[4].append(val)

               #if value is in third sub-box within rows 3-5, add it to sub-box list 5
               elif (j > 5 and j <= 8):
                  subBox[5].append(val)

            elif (i > 5 and i <= 8): #if we r on row 6-8, we want to add to sub-box 6-8 ================ OUTER 6-8 ================================

               #if value is in first sub-box within rows 6-8, add it to sub-box list 6
               if (j <=2):
                  subBox[6].append(val)

               #if value is in second sub-box within rows 6-8, add it to sub-box list 7
               elif (j > 2 and j <= 5):
                  subBox[7].append(val)

               #if value is in third sub-box within a row, rows 6-8, add it to sub-box list 8
               elif (j > 5 and j <= 8):
                  subBox[8].append(val)

   #pprint.pprint(subBox) #for debugging if sub box list is coming out right

  #========================================================================== SUB-BOX CHECK ===============================================================================================

  #Gets the list which represents each sub-box of the board as box, m will function as index of boxes inside subBox
   for m, box in enumerate(subBox): 
        
      #need to get every value inside of each sub-box as item, n is index of values inside each sub-box
      for n, item in enumerate(box): 

         #CHECK IF VAL IS ACTUAL INT OR NOT, we don't need to check periods since they are considered empty spaces
         if (item != "."):

            #ROW check val against every other value inside same row for duplicates ========================================================================================== ROW
            #so we use from val's n index+1 to end of the row, since once a val is checked and cleared at index n, we wont need to check the same index again
            for p in range(n+1, len(box)):
            
               if (item == box[p]):

                  print(f"\n Duplicate value in SUB-BOX, at BOX: {m} and item: {n}, where val = {item}, and box[{n}][{p}] = {box[p]}\n" )

                  return False
   
   #if the entire board matrix is gone through and no duplicates were found, return true      
   return True   

"""Function to attempt finding the best empty cell to start from, starting with row or col with least amount of numbers, then sub-box if desparate? """
def findEasiestStart(board: list[list[str]]):

   possible_vals = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #need list of values to try in the empty cells later (to be sent to solver funcs later)

   filledRowsBoard = [ [], [], [], [], [], [], [], [], [] ] #need new list to store lists of all the values in each row, at least 9 since there is one val in every box
   filledColsBoard = [ [], [], [], [], [], [], [], [], [] ] #need new list to store lists of all the values in each column, at least 9 since there is one val in every box

   filledSubBox = [ [], [], [], [], [], [], [], [], [] ] #need new list to store lists of all the values in each sub-box, at least 9 since there is one val in every box

   boardMinusFilledRows = [ [], [], [], [], [], [], [], [], [] ]
   boardMinusFilledCols = [ [], [], [], [], [], [], [], [], [] ]
   boardMinusFilledBoxes = [ [], [], [], [], [], [], [], [], [] ]

   tempBiggestRow = None
   tempBiggestCol = None
   tempBiggestBox = None

   #Gets the list which represents each row of the board as row, i will function as index of rows inside board
   for i, row in enumerate(board): 
        
      #need to get every value inside of each row as val, j is index of vals inside each row
      for j, val in enumerate(row):  #look through board until first period is found

         if (board[i][j] != "."): #if val is NOT a period, put it in list to compare lists 

            #ROW CHECK val and place all real values in a list  ========================================================================================================= ROW
            #so put every real value we find in each row into a list for the rows
            filledRowsBoard[i].append(board[i][j])
            boardMinusFilledRows[i].append(board[i][j])

            #COL CHECK val and place all real values in a list  ========================================================================================================= COL
            #so put every real value we find in each col into a list for the rows
            filledColsBoard[j].append(board[i][j])
            boardMinusFilledCols[j].append(board[i][j])

            #SUB-BOX CHECK val and place all real values in a list for each sub-box  ==================================================================================== SUB-BOX
            index = (i // 3) * 3 + (j // 3) #use floor division to get index of which sub-box to put each val in
            filledSubBox[index].append(board[i][j])
            boardMinusFilledBoxes[index].append(board[i][j])

   print("\n Rows: \n")
   pprint.pprint(filledRowsBoard)
   print("\n Columns: \n")
   pprint.pprint(filledColsBoard)
   print("\n Boxes: \n")
   pprint.pprint(filledSubBox)

   print("\n Minus Rows: \n")
   pprint.pprint(boardMinusFilledRows)
   print("\n Minus Columns: \n")
   pprint.pprint(boardMinusFilledCols)
   print("\n Minus Boxes: \n")
   pprint.pprint(boardMinusFilledBoxes)

   #once all the lists are filled, we need to count the lengths and get the list with the highest amount of values filled in to use as our starting point
   #WE WANT ONLY LISTS THAT ARE NOT FILLED, so limit max to be less than 9
   biggestRow = max(filledRowsBoard, key=len)
   indexBiggestRow = filledRowsBoard.index(biggestRow)

   while (len(biggestRow) == 9 ): #if biggest row is now 9 AS IN IT HAS BEEN FILLED, then we need to find the next biggest row

      removedRow = boardMinusFilledRows.pop(indexBiggestRow) #remove the biggest row we found in order to find the next biggest

      tempBiggestRow = max(boardMinusFilledRows, key=len) #get new biggest in line from list without the filled row

      #filledRowsBoard.insert(indexBiggestRow, removedRow) #re-insert previous row so that the indexes match up

      indexBiggestRow = filledRowsBoard.index(tempBiggestRow) #set index of row in original list of rows to send to solver

      biggestRow = tempBiggestRow #change biggest row if needed

   biggestCol = max(filledColsBoard, key=len)
   indexBiggestCol = filledColsBoard.index(biggestCol)

   while (len(biggestCol) == 9 ): #if biggest col is now 9 AS IN IT HAS BEEN FILLED, then we need to find the next biggest col

      del boardMinusFilledCols[indexBiggestCol] #remove the biggest row we found in order to find the next biggest

      tempBiggestCol = max(boardMinusFilledCols, key=len) #get new biggest in line from list without the filled col

      #filledColsBoard.insert(indexBiggestCol, removedCol) #re-insert previous col so that the indexes match up

      indexBiggestCol = filledColsBoard.index(tempBiggestCol) #set index of col in original list of cols to send to solver

      biggestCol = tempBiggestCol #change biggest col if needed


   biggestBox = max(filledSubBox, key=len)
   indexBiggestBox = filledSubBox.index(biggestBox)

   while (len(biggestBox) == 9 ): #if biggest box is now 9 AS IN IT HAS BEEN FILLED, then we need to find the next biggest box

      removedBox = boardMinusFilledBoxes.pop(indexBiggestBox) #remove the biggest box we found in order to find the next biggest

      tempBiggestBox = max(boardMinusFilledBoxes, key=len) #get new biggest in line from list without the filled box

      #filledSubBox.insert(indexBiggestBox, removedBox) #re-insert previous col so that the indexes match up

      indexBiggestBox = filledSubBox.index(tempBiggestBox) #set index of box in original list of boxes to send to solver

      biggestBox = tempBiggestBox #change biggest col if needed


   #print(f"Biggest Row: {indexBiggestRow}, with length of {len(biggestRow)}, Biggest Column: {indexBiggestCol}, with length of {len(biggestCol)}, Biggest Box: {indexBiggestBox}, with length of {len(biggestBox)}")
   
   #get biggest val of the three, then get the coordinate of it to determine where to start changing values in sudokuSolve()
   if (len(biggestRow) >= len(biggestCol) and len(biggestRow) >= len(biggestBox)): #================================================================ BIGGEST ROW
      print(f"\n Start with Row {indexBiggestRow}, since it is the biggest or equal to biggest list, with a value of {len(biggestRow)}.")

      #generate the remaining values that need to be tried, by finding the items in possible vals that aren't in the column's list
      remainingVals = [item for item in possible_vals if item not in filledRowsBoard[indexBiggestRow]]
      print(f" Row Contains: {filledRowsBoard[indexBiggestRow]}\n Remaining Values: {remainingVals}\n")

      sudokuSolveRow(board, indexBiggestRow, remainingVals)

      print("\n Row: ",indexBiggestRow, " was solved. Returning to main func.")

   elif (len(biggestCol) >= len(biggestRow) and len(biggestCol) >= len(biggestBox)): #============================================================== BIGGEST COL
      print(f"\n Start with Col {indexBiggestCol}, since it is the biggest or equal to biggest list, with a value of {len(biggestCol)}.")

      #generate the remaining values that need to be tried, by finding the items in possible vals that aren't in the column's list
      remainingVals = [item for item in possible_vals if item not in filledColsBoard[indexBiggestCol]]
      print(f" Column Contains: {filledColsBoard[indexBiggestCol]}\n Remaining Values: {remainingVals}\n")

      sudokuSolveCol(board, indexBiggestCol, remainingVals)

      print("\n Column: ",indexBiggestCol, " was solved. Returning to main func.")



   elif (len(biggestBox) >= len(biggestRow) and len(biggestBox) >= len(biggestCol)): #=============================================================== BIGGEST BOX
      print(f"\n Start with Box {indexBiggestBox}, since it is the biggest or equal to biggest list, with a value of {len(biggestBox)}.")

      #generate the remaining values that need to be tried, by finding the items in possible vals that aren't in the column's list
      remainingVals = [item for item in possible_vals if item not in filledBoxBoard[indexBiggestBox]]
      print(f" Box Contains: {filledBoxBoard[indexBiggestBox]}\n Remaining Values: {remainingVals}\n")

      sudokuSolveBox(board, indexBiggestBox, remainingVals)

      print("\n Box: ",indexBiggestBox, " was solved. Returning to main func.")



"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveRow(board: list[list[str]], bigRowIndex, startingVals):

   temp_row_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   for j in range(9): #look through board until first period is found

      newRowValWorks = False #define this value as false every time a new value is checked
      deadEnd = False #if deadEnd is found, then stop trying current order of values

      if (board[bigRowIndex][j] == "."): #find every period in the row sent to be solved

         while (newRowValWorks == False and deadEnd == False): 
         #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

            for index, x in enumerate(startingVals):

               temp_row_board[bigRowIndex][j] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

               tRowBoardIsValid = validityChecker(temp_row_board) #pass temp board once so that it doesnt run every if statement below

               if (tRowBoardIsValid == True):
                  #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                  board[bigRowIndex][j] = str(x) #actually change board and then trigger while loop to end
                  #pprint.pprint(temp_board)
                  pprint.pprint(board)
                  newRowValWorks = True
                  break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

               elif (tRowBoardIsValid == False and index == (len(startingVals)-1) and j != 8):

                  deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, dead end reached at row {bigRowIndex}, col {j}, exiting loop and closing program...\n Final Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                  board = copy.deepcopy(board_backup)
                  newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the row

                  print("\n Starting Values: ",startingVals, "\n NewStart: ", newStart, "\n")

                  sudokuSolveRow(board, bigRowIndex, newStart)

                  return #exit for loop so that it doesn't try any more values after dead end is reached

               elif (tRowBoardIsValid == False and index == (len(startingVals)-1) and j == 8):

                  noSolutionFound = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, no solution found for the row {bigRowIndex}, exiting program...\n Final Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  return 

            #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

      #AFTER WHILE LOOP AND FOR LOOP ENDS, should only run on final lap of for loop since j == 8
      #if end of row and end of possible inputs is reached, and board is valid, then row must be correct, so print out correct version of board and return to exit func
      if (board[bigRowIndex][j] != "." and j == 8):
         print(f"\n Row completed! Sending board to next starting point...\n New Board Being Sent: \n")
         pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

         findEasiestStart(board)

   #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.


"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveCol(board: list[list[str]], bigColIndex, startingVals):

   temp_col_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   for i in range(9): #look through board until first period is found

      newColValWorks = False #define this value as false every time a new value is checked
      deadEnd = False #if deadEnd is found, then stop trying current order of values

      if (board[i][bigColIndex] == "."): #find every period in the col sent to be solved

         while (newColValWorks == False and deadEnd == False): 
         #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

            for index, x in enumerate(startingVals):

               temp_col_board[i][bigColIndex] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

               tColBoardIsValid = validityChecker(temp_col_board) #pass temp board once so that it doesnt run every if statement below

               if (tColBoardIsValid == True):
                  #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                  board[i][bigColIndex] = str(x) #actually change board and then trigger while loop to end
                  #pprint.pprint(temp_board)
                  pprint.pprint(board)
                  newColValWorks = True
                  break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

               elif (tColBoardIsValid == False and index == (len(startingVals)-1) and i != 8):

                  deadEnd = True #if we tried all possible numbers 1-9 and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, dead end reached at row {i}, col {bigColIndex}, exiting loop and trying next combo...\n Dead End Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  temp_col_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                  board = copy.deepcopy(board_backup)
                  newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the column

                  print("\n Starting Values: ",startingVals, "\n NewStart: ", newStart, "\n")

                  sudokuSolveCol(board, bigColIndex, newStart)

                  return #exit for loop so that it doesn't try any more values after dead end is reached

               elif (tColBoardIsValid == False and index == (len(startingVals)-1) and i == 8):

                  noSolutionFound = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, no solution found for the column {bigColIndex}, exiting program...\n Final Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  return 

            #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

      #AFTER WHILE LOOP ENDS, not for loop, should only run on final lap of for loop since i == 8
      #if end of column and end of possible inputs is reached, and board is valid, then column must be correct, so print out correct version of board and return to exit func
      if (board[i][bigColIndex] != "." and i == 8):
         print(f"\n Column completed! Sending board to next starting point...\n New Board Being Sent: \n")
         pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

         findEasiestStart(board)

                  
   #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveBox(board: list[list[str]], bigBoxIndex, startingVals):

   temp_box_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   for m in range(3): #look through box until first period is found

      for n in range(3): 

         newBoxValWorks = False #define this value as false every time a new value is checked
         deadEnd = False #if deadEnd is found, then stop trying current order of values
         box_MIndex = 0 #define early so can use later
         box_NIndex = 0 #define early so can use later

         if (bigBoxIndex == 0 or bigBoxIndex == 3 or bigBoxIndex == 6):

            box_MIndex = bigBoxIndex + m #need coordinates to start at (0,0), (3,0), or (6,0)

            if (board[box_MIndex][n] == "."): #find every period in the box sent to be solved

               while (newBoxValWorks == False and deadEnd == False): 
               #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

                  for index, x in enumerate(startingVals):

                     temp_box_board[box_MIndex][n] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

                     tBoxBoardIsValid = validityChecker(temp_box_board) #pass temp board once so that it doesnt run every if statement below

                     if (tBoxBoardIsValid == True):
                        #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                        board[box_MIndex][n] = str(x) #actually change board and then trigger while loop to end
                        #pprint.pprint(temp_board)
                        pprint.pprint(board)
                        newBoxValWorks = True
                        break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

                     elif (tBoxBoardIsValid == False and index == (len(startingVals)-1) and m != 2):

                        deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, dead end reached at box {box_MIndex}, col {n}, exiting loop and closing program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                        board = copy.deepcopy(board_backup)
                        newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the row

                        print("\n Starting Values: ",startingVals, "\n NewStart: ", newStart, "\n")

                        sudokuSolveBox(board, bigBoxIndex, newStart)

                        return #exit for loop so that it doesn't try any more values after dead end is reached

                     elif (tBoxBoardIsValid == False and index == (len(startingVals)-1) and j == 8):

                        noSolutionFound = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, no solution found for the box {bigBoxIndex}, exiting program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        return 

                  #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            #AFTER WHILE LOOP AND FOR LOOP ENDS, should only run on final lap of for loop since m == 2
            #if end of box and end of possible inputs is reached, and board is valid, then row must be correct, so print out correct version of board and return to exit func
            if (board[box_MIndex][n] != "." and m == 2):
               print(f"\n Box completed! Sending board to next starting point...\n New Board Being Sent: \n")
               pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

               findEasiestStart(board)

         elif (bigBoxIndex == 1 or bigBoxIndex == 4 or bigBoxIndex == 7):

            box_MIndex = m + (bigBoxIndex - 1) #need coordinates to start at (0,3), (3,3), or (6,3)
            box_NIndex = 3 + n #need coordinates to start at (0,3), (3,3), or (6,3)

            if (board[box_MIndex][box_NIndex] == "."): #find every period in the box sent to be solved

               while (newBoxValWorks == False and deadEnd == False): 
               #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

                  for index, x in enumerate(startingVals):

                     temp_box_board[box_MIndex][box_NIndex] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

                     tBoxBoardIsValid = validityChecker(temp_box_board) #pass temp board once so that it doesnt run every if statement below

                     if (tBoxBoardIsValid == True):
                        #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                        board[box_MIndex][box_NIndex] = str(x) #actually change board and then trigger while loop to end
                        #pprint.pprint(temp_board)
                        pprint.pprint(board)
                        newBoxValWorks = True
                        break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

                     elif (tBoxBoardIsValid == False and index == (len(startingVals)-1) and m != 2):

                        deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, dead end reached at box {bigBoxIndex}, at row {box_MIndex}, col {box_NIndex}, exiting loop and closing program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                        board = copy.deepcopy(board_backup)
                        newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the row

                        print("\n Starting Values: ",startingVals, "\n NewStart: ", newStart, "\n")

                        sudokuSolveRow(board, bigBoxIndex, newStart)

                        return #exit for loop so that it doesn't try any more values after dead end is reached

                     elif (tBoxBoardIsValid == False and index == (len(startingVals)-1) and m == 2):

                        noSolutionFound = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, no solution found for the box {bigBoxIndex}, exiting program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        return 

                  #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            #AFTER WHILE LOOP AND FOR LOOP ENDS, should only run on final lap of for loop since m == 2
            #if end of box and end of possible inputs is reached, and board is valid, then row must be correct, so print out correct version of board and return to exit func
            if (board[box_MIndex][box_NIndex] != "." and m == 2):
               print(f"\n Box completed! Sending board to next starting point...\n New Board Being Sent: \n")
               pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

               findEasiestStart(board)

         elif (bigBoxIndex == 2 or bigBoxIndex == 5 or bigBoxIndex == 8):

            box_MIndex = m + (bigBoxIndex - 2) #need coordinates to start at (0,6), (3,6), or (6,6)
            box_NIndex = 6 + n 

            if (board[box_MIndex][box_NIndex] == "."): #find every period in the box sent to be solved

               while (newBoxValWorks == False and deadEnd == False): 
               #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

                  for index, x in enumerate(startingVals):

                     temp_box_board[box_MIndex][box_NIndex] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

                     tBoxBoardIsValid = validityChecker(temp_box_board) #pass temp board once so that it doesnt run every if statement below

                     if (tBoxBoardIsValid == True):
                        #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                        board[box_MIndex][box_NIndex] = str(x) #actually change board and then trigger while loop to end
                        #pprint.pprint(temp_board)
                        pprint.pprint(board)
                        newBoxValWorks = True
                        break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

                     elif (tBoxBoardIsValid == False and index == (len(startingVals)-1) and m != 2):

                        deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, dead end reached at box {bigBoxIndex}, at row {box_MIndex}, col {box_NIndex}, exiting loop and closing program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                        board = copy.deepcopy(board_backup)
                        newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the row

                        print("\n Starting Values: ",startingVals, "\n NewStart: ", newStart, "\n")

                        sudokuSolveRow(board, bigBoxIndex, newStart)

                        return #exit for loop so that it doesn't try any more values after dead end is reached

                     elif (tBoxBoardIsValid == False and index == (len(startingVals)-1) and m == 2):

                        noSolutionFound = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, no solution found for the box {bigBoxIndex}, exiting program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        return 

                  #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            #AFTER WHILE LOOP AND FOR LOOP ENDS, should only run on final lap of for loop since m == 2
            #if end of box and end of possible inputs is reached, and board is valid, then row must be correct, so print out correct version of board and return to exit func
            if (board[box_MIndex][box_NIndex] != "." and m == 2):
               print(f"\n Box completed! Sending board to next starting point...\n New Board Being Sent: \n")
               pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

               findEasiestStart(board)

   #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

def main():
   print("=" * 50)
   print(" Valid Sudoku EXERCISE")
   print("=" * 50)

   board1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

   print("\n Input board 1: ") #print board1 to console,
   pprint.pprint(board1)
   print("-" * 50)

   print("\n Output:") #print output of validity of board1
   print("-" * 50)
   #print("\n", sudokuSolve(board1))
   print("\n", findEasiestStart(board1))
   #print("\n", validityChecker(board1)) #send board1 to validity checker func to return if it is valid or not


   """

   board2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["5",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

   print("\n Input board 2: ") #print board2 to console,
   pprint.pprint(board2)
   print("-" * 50)

   print("\n Output:") #print output of validity of board2
   print("-" * 50)
   print("\n", validityChecker(board2)) #send board1 to validity checker func to return if it is valid or not

   #=========================================================== Board 1 SOLVED ========================================
   board3 = [["5","3","4","6","7","8","9","1","2"]
            ,["6","7","2","1","9","5","3","4","8"]
            ,["1","9","8","3","4","2","5","6","7"]
            ,["8","5","9","7","6","1","4","2","3"]
            ,["4","2","6","8","5","3","7","9","1"]
            ,["7","1","3","9","2","4","8","5","6"]
            ,["9","6","1","5","3","7","2","8","4"]
            ,["2","8","7","4","1","9","6","3","5"]
            ,["3","4","5","2","8","6","1","7","9"]]

   print("\n Input board 3: ") #print board3 to console,
   pprint.pprint(board3)
   print("-" * 50)

   print("\n Output:") #print output of validity of board3
   print("-" * 50)
   print("\n", validityChecker(board3)) #send board3 to validity checker func to return if it is valid or not
   """
if __name__ == "__main__":
   main()










"""
def sudokuSolve(board: list[list[str]]):

   temp_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work

   for i in range(9):

      for j in range(9): #look through board until first period is found

         newValWorks = False #define this value as false every time a new value is checked

         if (board[i][j] == "."): #if found a period, replace it with a number and check validity

            while (newValWorks == False): 
            #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

               for x in range(1,10):

                  temp_board[i][j] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

                  if (validityChecker(temp_board) == True):
                     #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                     board[i][j] = str(x) #actually change board and then trigger while loop to end
                     #pprint.pprint(temp_board)
                     pprint.pprint(board)
                     newValWorks = True
                     break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

                  elif (validityChecker(temp_board) == False and x == 9):

                     deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                     print(f"\nSorry, dead end reached at row {i}, col {j}, exiting loop and closing program...\nFinal Board: \n")
                     pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                     return

               #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

   #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

"""
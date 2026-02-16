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

#IMPORT TOOLS ======================================================================================

import pprint #want this to print out the sudoku boards in more readable format

import copy #need a way to create an entirely new copy of the game board which will be altered first to avoid overwriting the actual game board, and ".copy()" isn't good enough for a list of lists

import itertools #need .permutations() in order to get each solver function to try every possible combo of numbers

import sys #using sys.exit() once board is filled either correctly or incorrectly to avoid the backwards recursive calls

#IMPORT MY OTHER FUNCTIONS ======================================================================================

import validityChecker

import sudokuSolveRow

import sudokuSolveCol

import sudokuSolveBox



"""Function to attempt finding the best empty cell to start from, starting with row or col with least amount of numbers, then sub-box if desparate? """
def findEasiestStart(board: list[list[str]], skipRows, skipCols, skipBoxes):

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

   rowsFilled = False
   colsFilled = False
   boxesFilled = False

   potentiallyFinalBoardIsValid = None #none because it is deteremined by the validityChecker function

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
   """
   print("\n Rows: \n")
   pprint.pprint(filledRowsBoard)
   print("\n Columns: \n")
   pprint.pprint(filledColsBoard)
   print("\n Boxes: \n")
   pprint.pprint(filledSubBox)
   """

   #once all the lists are filled, we need to count the lengths and get the list with the highest amount of values filled in to use as our starting point
   #WE WANT ONLY LISTS THAT ARE NOT FILLED, so limit max to be less than 9
   biggestRow = max(filledRowsBoard, key=len)
   indexBiggestRow = filledRowsBoard.index(biggestRow)

   while (len(biggestRow) == 9 ): #if biggest row is now 9 AS IN IT HAS BEEN FILLED, then we need to find the next biggest row

      boardMinusFilledRows[indexBiggestRow] = [] #remove the biggest row we found in order to find the next biggest

      tempBiggestRow = max(boardMinusFilledRows, key=len) #get new biggest in line from list without the filled row

      #filledRowsBoard.insert(indexBiggestRow, removedRow) #re-insert previous row so that the indexes match up

      if (len(tempBiggestRow) != 0): #as long as the biggest row is not empty BEFORE SKIPS, if it is, the board is complete or we are out of rows to try

         indexBiggestRow = filledRowsBoard.index(tempBiggestRow) #set index of row in original list of rows to send to solver

         biggestRow = tempBiggestRow #change biggest row if needed

      elif (len(tempBiggestRow) == 0): #if the biggest row is empty BEFORE SKIPS, it means we are out of rows to fill, they must all be filled at this point, since boardMinusRows will only contain the real values in each row or an empty list for each filled row

         print(f"\n While checking for the biggest row that isn't filled before it skips any rows, it found\n an empty list to be the biggestRow, so it should mean that every row has been filled by this point, since it hasn't\n been told which rows to skip yet, its only empting every filled row...")

         rowsFilled = True #trigger bool to be evaluated below

         indexBiggestRow = 0 #force biggest index to be 0 since we dont want to compare the real values on the board anymore
         biggestRow = tempBiggestRow #force biggest row to stay empty since we want the logic to check the column and box list for a bigger list to be sure that the board is full

   #if we found more than one option for a row, we want to skip those rows and find the biggest value again
   if (len(skipRows) > 0):

      for x in skipRows:
         boardMinusFilledRows[x] = [] #remove skip rows from board being checked for biggest row

      tempBiggestRow = max(boardMinusFilledRows, key=len) #get new biggest in line from list without the skipped rows

      if (len(tempBiggestRow) != 0): #as long as the biggest row is not empty AFTER SKIPS, if it is, the board is complete or we are out of rows to try

         indexBiggestRow = filledRowsBoard.index(tempBiggestRow) #set index of row in original list of rows to send to solver

         biggestRow = tempBiggestRow #change biggest row if needed

      elif (len(tempBiggestRow) == 0): #if the biggest row is empty AFTER SKIPS, it means we are out of rows to fill, either they are filled or have been skipped at this point

         print(f"\n While checking for the biggest row that isn't filled after skipping certain rows, it found\n an empty list to be the biggestRow, so either the board is complete or every row has been either filled or skipped\n due to multiple solutions existing when they were evaluated...")

         indexBiggestRow = 0 #force biggest index to be 0 since we dont want to compare the real values on the board anymore
         biggestRow = tempBiggestRow #force biggest row to stay empty since we want the logic to check the column and box list for a bigger list to be sure that the board is full


   biggestCol = max(filledColsBoard, key=len) #get biggest current column
   indexBiggestCol = filledColsBoard.index(biggestCol)

   while (len(biggestCol) == 9 ): #if biggest col is now 9 AS IN IT HAS BEEN FILLED, then we need to find the next biggest col

      boardMinusFilledCols[indexBiggestCol] = [] #remove the biggest row we found in order to find the next biggest

      tempBiggestCol = max(boardMinusFilledCols, key=len) #get new biggest in line from list without the filled col

      #filledColsBoard.insert(indexBiggestCol, removedCol) #re-insert previous col so that the indexes match up

      if (len(tempBiggestCol) != 0): #as long as the biggest col is not empty BEFORE SKIPS, if it is, the board is complete or we are out of cols to try

         indexBiggestCol = filledColsBoard.index(tempBiggestCol) #set index of col in original list of cols to send to solver

         biggestCol = tempBiggestCol #change biggest col if needed

      elif (len(tempBiggestCol) == 0): 
         # if the biggest col is empty BEFORE SKIPS, it means we are out of cols to fill, they must all be filled at this point, since boardMinusCols will only contain
         # the real values in each col or an empty list for each filled col

         print(f"\n While checking for the biggest col that isn't filled before it skips any cols, it found\n an empty list to be the biggestCol, so it should mean that every col has been filled by this point, since it hasn't\n been told which cols to skip yet, its only empting every filled col...")

         indexBiggestCol = 0 #force biggest index to be 0 since we dont want to compare the real values on the board anymore
         biggestCol = tempBiggestCol #force biggest col to stay empty since we want the logic to check the row and box list for a bigger list to be sure that the board is full

   #if we found more than one option for a col, we want to skip those cols and find the biggest value again
   if (len(skipCols) > 0):

      for x in skipCols:
         boardMinusFilledCols[x] = [] #remove skip cols from board being checked for biggest col

      tempBiggestCol = max(boardMinusFilledCols, key=len) #get new biggest in line from list without the skipped cols

      if (len(tempBiggestCol) != 0): #as long as the biggest col is not empty AFTER SKIPS, if it is, the board is complete or we are out of cols to try

         indexBiggestCol = filledColsBoard.index(tempBiggestCol) #set index of col in original list of cols to send to solver

         biggestCol = tempBiggestCol #change biggest col if needed

      elif (len(tempBiggestCol) == 0): 
         # if the biggest col is empty AFTER SKIPS, it means we are out of cols to fill, they must all be filled at this point, since boardMinusCols will only contain
         # the real values in each col or an empty list for each filled col

         print(f"\n While checking for the biggest col that isn't filled after skipping certain cols, it found\n an empty list to be the biggestCol, so either the board is complete or every col has been either filled or skipped due\n to multiple solutions existing when they were evaluated...")

         indexBiggestCol = 0 #force biggest index to be 0 since we dont want to compare the real values on the board anymore
         biggestCol = tempBiggestCol #force biggest col to stay empty since we want the logic to check the row and box list for a bigger list to be sure that the board is full

   """
   # Had the logic to check boxes just like the row and col for a starting point, but commented out once I had changed the rows and cols code to work durastically different, 
   # now is not needed, and is casuing index issues once the board is filled

   biggestBox = max(filledSubBox, key=len)
   indexBiggestBox = filledSubBox.index(biggestBox)

   while (len(biggestBox) == 9 ): #if biggest box is now 9 AS IN IT HAS BEEN FILLED, then we need to find the next biggest box

      boardMinusFilledBoxes[indexBiggestBox] = [] #remove the biggest box we found in order to find the next biggest

      tempBiggestBox = max(boardMinusFilledBoxes, key=len) #get new biggest in line from list without the filled box

      #filledSubBox.insert(indexBiggestBox, removedBox) #re-insert previous col so that the indexes match up

      indexBiggestBox = filledSubBox.index(tempBiggestBox) #set index of box in original list of boxes to send to solver

      biggestBox = tempBiggestBox #change biggest col if needed
   """

   print("\n Minus Rows After While and Skip Loops: \n")
   pprint.pprint(boardMinusFilledRows)
   print("\n Minus Column After While and Skip Loops: \n")
   pprint.pprint(boardMinusFilledCols)

   """
   print("\n Minus Boxes After While and Skip Loops: \n")
   pprint.pprint(boardMinusFilledBoxes)
   """

   #print(f"Biggest Row: {indexBiggestRow}, with length of {len(biggestRow)}, Biggest Column: {indexBiggestCol}, with length of {len(biggestCol)}, Biggest Box: {indexBiggestBox}, with length of {len(biggestBox)}")
   #and len(biggestRow) >= len(biggestBox)
   #and len(biggestCol) >= len(biggestBox)
   #get biggest val of the three, then get the coordinate of it to determine where to start changing values in sudokuSolve()
   if (len(biggestRow) >= len(biggestCol)): #================================================================ BIGGEST ROW

      if (len(biggestRow) != 0): #if biggest row is NOT an empty list, then find all the possible vals needed to fill it and send it to be solved
         print(f"\n Start with Row {indexBiggestRow}, since it is the biggest or equal to biggest list, with a value of {len(biggestRow)}.")

         #generate the remaining values that need to be tried, by finding the items in possible vals that aren't in the column's list
         remainingVals = [item for item in possible_vals if item not in filledRowsBoard[indexBiggestRow]]
         print(f" Row Contains: {filledRowsBoard[indexBiggestRow]}\n Remaining Values: {remainingVals}\n")

         allPossibleVals = list(itertools.permutations(remainingVals)) #generate list of lists where each list is a different combo of the remaingvals to fill the row

         sudokuSolveRow.sudokuSolveRow(board, indexBiggestRow, allPossibleVals, 0, [ ], 0, skipRows, skipCols, skipBoxes)

         print("\n Row: ",indexBiggestRow, " was attemped...Returning to main func.")
         return

      elif (len(biggestRow) == 0): #if biggest row IS an empty list, then we are out of rows and columns to try, since to get here and have biggestRow be empty, it means the biggestCol is also empty

         print("\n Hey! It looks like both the rows are columns are filled or have been skipped...\n Need to perform final checks... Checking if the board is filled...\n Current Board:\n")

         pprint.pprint(board)

         emptyCells = 0 #need to count how many empty cells are found to see if board is filled or not

         #NEED TO CHECK BOARD HAS NO EMPTY SPACES ONE LAST TIME
         #Gets the list which represents each row of the board as row, r will function as index of rows inside board
         for r, row in enumerate(board): 
        
            #need to get every value inside of each row as val, v is index of vals inside each row
            for v, val in enumerate(row):

               if (val == "."): #If we found a period we need to send the row that it is in to be solved...

                  print(f"\n Oops! It looks like we found a period still on the board in row {r}, col {v}, sending it to be solved now...")

                  emptyCells += 1 #board is still not filled! Need to fix it below

                  indexEmptyRowFound = r

         #IF FOUND PERIOD AFTER FORS, SEND BOARD TO BE SOLVED
         if (emptyCells > 0):
            #generate the remaining values that need to be tried, by finding the items in possible vals that aren't in the column's list
            remainingVals = [item for item in possible_vals if item not in filledRowsBoard[indexEmptyRowFound]]
            print(f"\n Row {indexEmptyRowFound} Contains: {filledRowsBoard[indexEmptyRowFound]}\n Remaining Values: {remainingVals}\n")

            allPossibleVals = list(itertools.permutations(remainingVals)) #generate list of lists where each list is a different combo of the remaingvals to fill the row

            sudokuSolveRow.sudokuSolveRow(board, indexEmptyRowFound, allPossibleVals, 0, [ ], 0, skipRows, skipCols, skipBoxes)

            print("\n Row: ",indexEmptyRowFound, " was attemped...Returning to main func.")

         #IF BOARD HAS ZERO PERIODS in it, it must be filled, so perform last check!
         elif (emptyCells == 0): 
            print("\n Hey! It looks like the board is full... Checking if the board is valid...")

            potentiallyFinalBoardIsValid = validityChecker.validityChecker(board) #pass board to validity checker 

            if (potentiallyFinalBoardIsValid == True):
               print("\n Hey we did it! The board has been filled and solved according to the validity checker! Congrats! Final Board:\n")
               pprint.pprint(board)
               print("\n Exiting the entire program...")
               sys.exit()

            elif (potentiallyFinalBoardIsValid == False):

               print("Sorry! It looks like we filled the board, but it looks like the final board we have as a result isn't actually valid.\n So either the board is not actually solvable, or a mistake was made somewhere along the way...")
               print("\n Final Board:\n")
               pprint.pprint(board)
               print("\n Exiting the entire program...")
               sys.exit()


   elif (len(biggestCol) >= len(biggestRow)): #============================================================== BIGGEST COL

      if (len(biggestCol) != 0): #if biggest col is NOT an empty list, then find all the possible vals needed to fill it and send it to be solved
         print(f"\n Start with Col {indexBiggestCol}, since it is the biggest or equal to biggest list, with a value of {len(biggestCol)}.")

         #generate the remaining values that need to be tried, by finding the items in possible vals that aren't in the column's list
         remainingVals = [item for item in possible_vals if item not in filledColsBoard[indexBiggestCol]]
         print(f" Column Contains: {filledColsBoard[indexBiggestCol]}\n Remaining Values: {remainingVals}\n")

         allPossibleVals = list(itertools.permutations(remainingVals)) #generate list of lists where each list is a different combo of the remaingvals to fill the column

         sudokuSolveCol.sudokuSolveCol(board, indexBiggestCol, allPossibleVals, 0, [ ], 0, skipRows, skipCols, skipBoxes)

         print("\n Column: ",indexBiggestCol, " was attemped...Returning to main func.")

      elif (len(biggestCol) == 0): #if biggest col IS an empty list, but we should never get here since the if comparing biggestCol is bigger than biggestRow shouldn't ever come true if biggestCol = 0

         print(" Hey! Something might have gone wrong, it found biggestCol to be >= biggestRow but then also found biggestCol to be an empty list, \n but the biggestRow if would be true before it gets here...")


"""
   elif (len(biggestBox) >= len(biggestRow) and len(biggestBox) >= len(biggestCol)): #=============================================================== BIGGEST BOX
      print(f"\n Start with Box {indexBiggestBox}, since it is the biggest or equal to biggest list, with a value of {len(biggestBox)}.")

      #generate the remaining values that need to be tried, by finding the items in possible vals that aren't in the column's list
      remainingVals = [item for item in possible_vals if item not in filledSubBox[indexBiggestBox]]
      print(f" Box Contains: {filledSubBox[indexBiggestBox]}\n Remaining Values: {remainingVals}\n")

      sudokuSolveBox(board, indexBiggestBox, remainingVals)

      print("\n Box: ",indexBiggestBox, " was solved. Returning to main func.")
"""




def main():
   print("=" * 50)
   print(" Sudoku Find Easiest Start Function:")
   print("=" * 50)

   """board1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

      boardHMCOMPLETED = [["5","4","3","9","8","6","1","2","7"]
                         ,["9","7","2","1","3","5","4","8","6"]
                         ,["6","1","8","2","7","4","3","5","9"]
                         ,["7","5","1","6","2","8","9","4","3"]
                         ,["8","3","4","7","9","1","2","6","5"]
                         ,["2","6","9","5","4","3","7","1","8"]
                         ,["4","9","6","8","1","7","5","3","2"]
                         ,["3","2","5","4","6","9","8","7","1"]
                         ,["1","8","7","3","5","2","6","9","4"]]
   """

   boardHARDMODE = [["5","4",".","9","8","6","1","2","7"]
                   ,["9",".","2",".","3",".",".",".","."]
                   ,[".",".",".","2",".",".","3",".","."]
                   ,[".",".","1","6","2",".",".",".","."]
                   ,["8","3","4","7","9",".","2",".","5"]
                   ,[".",".","9",".","4","3","7",".","."]
                   ,[".",".","6",".",".","7",".",".","."]
                   ,[".",".","5",".","6",".",".",".","1"]
                   ,["1",".",".",".","5","2",".","9","4"]]

   print("\n Input board 1: ") #print board1 to console,
   pprint.pprint(boardHARDMODE)
   print("-" * 50)

   print("\n Output:") #print output of validity of board1
   print("-" * 50)
   #print("\n", sudokuSolve(board1))
   print("\n", findEasiestStart(boardHARDMODE, [], [], []))
   #print("\n", validityChecker(board1)) #send board1 to validity checker func to return if it is valid or not


   
if __name__ == "__main__":
   main()






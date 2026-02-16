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

import itertools #need .permutations() in order to get each solver function to try every possible combo of numbers

import sys #using sys.exit() once board is filled either correctly or incorrectly to avoid the backwards recursive calls

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
   # now is not needed  and is casuing index issues once the board is filled

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

         sudokuSolveRow(board, indexBiggestRow, allPossibleVals, 0, [ ], 0, skipRows, skipCols, skipBoxes)

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

            sudokuSolveRow(board, indexEmptyRowFound, allPossibleVals, 0, [ ], 0, skipRows, skipCols, skipBoxes)

            print("\n Row: ",indexEmptyRowFound, " was attemped...Returning to main func.")

         #IF BOARD HAS ZERO PERIODS in it, it must be filled, so perform last check!
         elif (emptyCells == 0): 
            print("\n Hey! It looks like the board is full... Checking if the board is valid...")

            potentiallyFinalBoardIsValid = validityChecker(board) #pass board to validity checker 

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

         sudokuSolveCol(board, indexBiggestCol, allPossibleVals, 0, [ ], 0, skipRows, skipCols, skipBoxes)

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



"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveRow(board: list[list[str]], bigRowIndex, startingVals, deadEndCount, possibleRowOrder, pRowOrderCount, skipRows, skipCols, skipBoxes) -> []:

   temp_row_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   tempPossibleRow = [ ]

   print("\n Starting Values at beginning of SolveRow: ",startingVals[deadEndCount], "DeadEndCount:",deadEndCount, "\n")

   for j in range(9): #look through board until first period is found

      newRowValWorks = False #define this value as false every time a new value is checked
      deadEnd = False #if deadEnd is found, then stop trying current order of values

      if (board[bigRowIndex][j] == "."): #find every period in the row sent to be solved

         while (newRowValWorks == False and deadEnd == False and deadEndCount != len(startingVals) ): 
         #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

            for index, x in enumerate(startingVals[deadEndCount]): #only check each values in one set of values at a time, index by 

               temp_row_board[bigRowIndex][j] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

               tRowBoardIsValid = validityChecker(temp_row_board) #pass temp board once so that it doesnt run every if statement below

               if (tRowBoardIsValid == True):
                  #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                  board[bigRowIndex][j] = str(x) #actually change board and then trigger while loop to end
                  #pprint.pprint(temp_board)
                  pprint.pprint(board)
                  newRowValWorks = True
                  break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

               elif (tRowBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and j <= 8):

                  deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, dead end reached at row {bigRowIndex}, col {j}, exiting loop and attempting to try next combo...\n Dead End Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                  board = copy.deepcopy(board_backup)
                  #newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the row

                  deadEndCount += 1 #add one to count how many dead ends have been hit, once count equals how many values are in startingvals, we have tried every combo we could

                  if (deadEndCount <= (len(startingVals)-1)):  #if we still have other combos to try, increment deadEndCount and move on to next combo
                     print(" Starting Values: ",startingVals[deadEndCount-1], "\n New Starting Values: ", startingVals[deadEndCount], "\n")

                     print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                     #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
                     possibleRowOrder = sudokuSolveRow(board, bigRowIndex, startingVals, deadEndCount, possibleRowOrder, pRowOrderCount, skipRows, skipCols, skipBoxes ) 

                     return possibleRowOrder #exit function after returning from recursive solveRow call, so that it doesn't try any more values after dead end is reached

                  elif (deadEndCount > (len(startingVals)-1) and pRowOrderCount == 0): #if we finish trying a combo before we get to the last item in the row, and we are out of combos
                     #if we have tried the last value in the last combo of values, and we have 0 possible solutions, we need to quit since we have run out of possible combinations to try
                     print("\n Sorry! We have tried every possible combination of values on row ", bigRowIndex, ".\n This means the board is not solvable, or that we made a mistake somewhere...\n")
                     print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )
                     print("\n Exiting Function...")
                     return possibleRowOrder #exit function without calling solveRow again, since we have reached a full deadend without any solutions

                  elif (deadEndCount > (len(startingVals)-1) and pRowOrderCount > 0): #if we finish trying a combo before we get to the last item in the row, and we are out of combos (j < 8)
                     #AND we have more than one possible solution, we need to properly return said list of solutions
                     print("\n We have now tried every possible combination of values on row", bigRowIndex, "\n")
                     print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                     break 
                     #if deadendCount maxed but we have solutions, we need to break from this for loop, which will break while loop, and then on the last check of j with full deadEndCount, 
                     #we will pick a combo. NOTE: if deadEndCount max hit before j is through entire row and the row ends in an empty cell, the ifs that this will go to won't work, since
                     #they need the last item in the row to be a actual number and not a "."

               elif (tRowBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and j == 8 and deadEndCount == len(startingVals) ):

                  noSolutionFound = True #if we tried all possible combinations of the values avaliable, and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, no solution found for the row {bigRowIndex}, exiting program...\n Final Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  return possibleRowOrder

         if (deadEndCount == len(startingVals) and pRowOrderCount == 0):

            noSolutionFound = True #if we tried all possible combinations of the values avaliable, and board is not coming out right, trigger the dead end and try new numbers?
            print(f"\n Sorry, no solution found for the row {bigRowIndex}, deadEndCount = {deadEndCount}, and startingVals Length = {len(startingVals)}, exiting program...\n Final Board: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            return possibleRowOrder


          #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

      #AFTER WHILE LOOP AND FOR LOOP ENDS, BUT STILL WITHIN J FOR, need to create list containing the valid order that was found and store it in big list containing all possible orders for this row
      #should only run on final lap of for loop since j == 8, and only when dead end count is not full
      #if at end of row and board is valid, then row must be correct, so add it to possible orders, and then if deadEndCount is still less than startingVals length, it means there is still combos to 
      #try, so we need to save the row's order and then try the other options
      if (board[bigRowIndex][j] != "." and j == 8 and deadEndCount != len(startingVals) ):

         print(f"\n Possible Row Order Found! Saving order to possibleRowOrder...\n Row Being Saved: {bigRowIndex} = {board[bigRowIndex]} ")

         for b in range(9):

            tempPossibleRow.append(board[bigRowIndex][b]) #loop through the complete row and add each val to list tempPossibleRow to be then stored inside possibleRowOrder list

         if tempPossibleRow not in possibleRowOrder: #we only want to add possible row order if it is different than the rest of already saved possible orders
            possibleRowOrder.append(tempPossibleRow) #add temp list to end of big list

            pRowOrderCount += 1 
            #after adding the UNIQUE completed row order to the list, we need to increment this so next time a possible order is found in the next call to this function, it can be added properly
            print(f" Unique solution found...tempPossibleRow: {tempPossibleRow}\n PossibleRowOrder: {possibleRowOrder}\n pOrderCount: {pRowOrderCount}")


         elif tempPossibleRow in possibleRowOrder:

            print("\n Oh! It looks like that possible order has already been saved to the list, so we aren't saving it, moving on... ")
            print(f" PossibleColOrder: {possibleRowOrder}\n pOrderCount: {pRowOrderCount}")

         board = copy.deepcopy(board_backup) #re write regular board back to starting point to try different order of numbers again
         
         #we should increment deadEndCount in order to check the next possible order of vals, otherwise it infintely checks just the first correct order
         deadEndCount += 1

         if (deadEndCount != len(startingVals) ):
            print(f"\n Checking next possible combination by sending updated deadEndCount({deadEndCount}) to SolveRow recursively...")
            #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
            allOrders = sudokuSolveRow(board, bigRowIndex, startingVals, deadEndCount, possibleRowOrder, pRowOrderCount, skipRows, skipCols, skipBoxes) 

            print("\n After saving possible row order",pRowOrderCount,", we have checked the rest of the startingvals and finished with", len(allOrders), "possible orders...")

            return allOrders #need to return the list of possible rows after 

         elif (deadEndCount == len(startingVals) ):

            print("\n So the row has finished checking every possible combination, it found", pRowOrderCount, "possible row order(s)...")

            print(f"\n PossibleRowOrder: {possibleRowOrder}")

            if (pRowOrderCount > 1):

               print(f"\n So row {bigRowIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

               skipRows.append(bigRowIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

               temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different order of numbers again
               board = copy.deepcopy(board_backup)

               findEasiestStart(board, skipRows, skipCols, skipBoxes)

            elif (pRowOrderCount == 1):

               #if row only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
               for y in range(9):

                  board[bigRowIndex][y] = possibleRowOrder[0][y] #re save only solution to board before sending the board with the completed row to next start

               print(f"\n Row completed with only possible combination! Sending board to next starting point...\n New Board Being Sent: \n")
               pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

               findEasiestStart(board, skipRows, skipCols, skipBoxes)


      #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, 
      elif (board[bigRowIndex][j] != "." and j == 8 and deadEndCount == len(startingVals) ):

         print(f"\n All possible orders of values for this row have been found...\n Checking if more than 2... There are", pRowOrderCount)

         if (pRowOrderCount > 1):

            print(f"\n So row: {bigRowIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

            skipRows.append(bigRowIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

            temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
            board = copy.deepcopy(board_backup)

            findEasiestStart(board, skipRows, skipCols, skipBoxes)

         elif (pRowOrderCount == 1):

            #if row only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
            for z in range(9):

               board[bigRowIndex][z] = possibleRowOrder[0][z] #re save only solution to board before sending the board with the completed row to next start

            print(f"\n Row completed with only possible combination! Sending board to next starting point...\n New Board Being Sent: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            findEasiestStart(board, skipRows, skipCols, skipBoxes)

      #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, AND THE DEADENDCOUNT IS MAXXED BEFORE FINISHING ROW
      elif (deadEnd == True and j <= 8 and deadEndCount == len(startingVals) ):

         print(f"\n All possible orders of values for this row have been tried...\n Checking how many possible... There are", pRowOrderCount)

         if (pRowOrderCount > 1):

            print(f"\n So row: {bigRowIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

            skipRows.append(bigRowIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

            temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
            board = copy.deepcopy(board_backup)

            findEasiestStart(board, skipRows, skipCols, skipBoxes)

         elif (pRowOrderCount == 1):

            #if row only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
            for q in range(9):

               board[bigRowIndex][q] = possibleRowOrder[0][q] #re save only solution to board before sending the board with the completed row to next start

            print(f"\n Row completed with only possible combination after checking every single combo! Sending board to next starting point...\n New Board Being Sent: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            findEasiestStart(board, skipRows, skipCols, skipBoxes)

         elif (pRowOrderCount < 1):

            print(f"\n Sorry, no possible combinations found for row {bigRowIndex} after trying all possible permutations and reaching a dead end before the end of said row,\n while the end of the row contains a '.' still...\n")
            return possibleRowOrder

   #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.


"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveCol(board: list[list[str]], bigColIndex, startingVals, deadEndCount, possibleColOrder, pColOrderCount, skipRows, skipCols, skipBoxes) -> []:

   temp_col_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   tempPossibleCol = [  ]

   print("\n Starting Values at beginning of SolveCol:",startingVals[deadEndCount], "DeadEndCount:",deadEndCount, "\n")

   for i in range(9): #look through board until first period is found

      newColValWorks = False #define this value as false every time a new value is checked
      deadEnd = False #if deadEnd is found, then stop trying current order of values

      if (board[i][bigColIndex] == "."): #find every period in the col sent to be solved

         while (newColValWorks == False and deadEnd == False and deadEndCount != len(startingVals) ): 
         #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

            for index, x in enumerate(startingVals[deadEndCount]):

               temp_col_board[i][bigColIndex] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

               tColBoardIsValid = validityChecker(temp_col_board) #pass temp board once so that it doesnt run every if statement below

               if (tColBoardIsValid == True):
                  #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                  board[i][bigColIndex] = str(x) #actually change board and then trigger while loop to end
                  #pprint.pprint(temp_board)
                  pprint.pprint(board)
                  newColValWorks = True
                  break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

               elif (tColBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and i <= 8):

                  deadEnd = True #if we tried all possible numbers in the current combo and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, dead end reached at row {i}, col {bigColIndex}, exiting loop and attempting to try next combo...\n Dead End Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  temp_col_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                  board = copy.deepcopy(board_backup)
                  #newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the column

                  deadEndCount += 1 #add one to count how many dead ends have been hit, once count equals how many values are in startingvals, we have tried every combo we could

                  if (deadEndCount <= (len(startingVals)-1) ):  #if we still have other combos to try, increment deadEndCount and move on to next combo
                     print("\n Starting Values: ", startingVals[deadEndCount-1], "\n New Starting Values: ", startingVals[deadEndCount], "\n")

                     print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                     sudokuSolveCol(board, bigColIndex, startingVals, deadEndCount, possibleColOrder, pColOrderCount, skipRows, skipCols, skipBoxes) #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list

                     return possibleColOrder #exit for loop so that it doesn't try any more values after dead end is reached

                  elif (deadEndCount > (len(startingVals)-1) and pColOrderCount == 0): 
                  #if we have tried the last value in the last combo of values, AND NO SOLUTION FOUND, we need to quit since we have run out of possible combinations to try
                     print("\n We have now tried every possible combination of values on column", bigColIndex, ".\n This means the board is not solvable, or that we made a mistake somewhere...\n")
                     print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )
                     print("\n Exiting Function...")
                     return possibleColOrder #exit function since we have reached a full deadend

                  elif (deadEndCount > (len(startingVals)-1) and pColOrderCount > 0): #if we finish trying a combo before we get to the last item in the col, and we are out of combos (i < 8)
                     #AND we have more than one possible solution, we need to properly return said list of solutions
                     print("\n We have now tried every possible combination of values on col", bigColIndex, ".\n")
                     print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                     break 
                     #if deadend hit but we have solutions, we need to break from this for loop, which will break while loop, and then on the last check of j with full deadEndCount, we will pick a combo

               elif (tColBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and i == 8 and deadEndCount == len(startingVals) ):

                  noSolutionFound = True #if we tried all possible combinations of the values avaliable, and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, no solution found for the column {bigColIndex}, exiting program...\n Final Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  return possibleColOrder

         if (deadEndCount == len(startingVals) and pColOrderCount == 0):

            noSolutionFound = True #if we tried all possible combinations of the values avaliable, and board is not coming out right, trigger the dead end and try new numbers?
            print(f"\n Sorry, no solution found for the col {bigColIndex}, deadEndCount = {deadEndCount}, and startingVals Length = {len(startingVals)}, exiting program...\n Final Board: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            return possibleColOrder

         #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

      #AFTER WHILE LOOP AND FOR LOOP ENDS, BUT STILL WITHIN i FOR, need to create list containing the valid order that was found and store it in big list containing all possible orders for this COL
      #should only run on final lap of for loop since i == 8, and only when dead end count is not full
      #if at end of col and board is valid, then col must be correct, so add it to possible orders, and then if deadEndCount is still less than startingVals length, it means there is still combos to 
      #try, so we need to save the col's order and then try the other options
      if (board[i][bigColIndex] != "." and i == 8 and deadEndCount != len(startingVals) ):

         print(f"\n Possible Column Order Found! Saving order to possibleColOrder...\n Col Being Saved: {bigColIndex} ")

         for b in range(9):

            tempPossibleCol.append(board[b][bigColIndex]) #loop through the complete col and add each val to list tempPossibleCol to be then stored inside possibleColOrder list

         if tempPossibleCol not in possibleColOrder: #we only want to add possible col order if it is different than the rest of already saved possible orders
            possibleColOrder.append(tempPossibleCol) #add temp list to end of big list

            pColOrderCount += 1 
            #after adding the UNIQUE completed col order to the list, we need to increment this so next time a possible order is found in the next call to this function, it can be added properly
            print(f" Unique solution found...tempPossibleCol: {tempPossibleCol}\n PossibleColOrder: {possibleColOrder}\n pOrderCount: {pColOrderCount}")

         elif tempPossibleCol in possibleColOrder:

            print("\n Oh! It looks like that possible order has already been saved to the list, so we aren't saving it, moving on... ")
            print(f" PossibleColOrder: {possibleColOrder}\n pOrderCount: {pColOrderCount}")


         board = copy.deepcopy(board_backup) #re write regular board back to starting point to try different order of numbers again

         #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
         #we should increment deadEndCount in order to check the next possible order of vals, otherwise it infintely checks just the first correct order
         deadEndCount += 1

         if (deadEndCount != len(startingVals) ):
            print(f"\n Checking next possible combination by sending updated deadEndCount({deadEndCount}) to SolveCol recursively...")
            allOrders = sudokuSolveCol(board, bigColIndex, startingVals, deadEndCount, possibleColOrder, pColOrderCount, skipRows, skipCols, skipBoxes) 

            print("\n After saving possible col order",pColOrderCount,"we have checked the rest of the startingvals and finished with ", len(allOrders), "possible orders...")

         elif (deadEndCount == len(startingVals) ): #if we have no more permutations to check after attempting to save the last possible order, we need to decide to fill the board or not

            print("\n So the column has finished checking every possible combination, it found", pColOrderCount, "possible column order(s)...")

            print(f"\n PossibleColOrder: {possibleColOrder}")

            if (pColOrderCount > 1):

               print(f"\n So column {bigColIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

               skipCols.append(bigColIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

               temp_col_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
               board = copy.deepcopy(board_backup)

               findEasiestStart(board, skipRows, skipCols, skipBoxes)

            elif (pColOrderCount == 1):
               #if column only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
               for y in range(9):

                  board[y][bigColIndex] = possibleColOrder[0][y] #re save only solution to board before sending the board with the completed col to next start


               print(f"\n Column completed with only possible combination! Sending board to next starting point...\n New Board Being Sent: \n")
               pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

               findEasiestStart(board, skipRows, skipCols, skipBoxes)

      #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleColOrder list, 
      elif (board[i][bigColIndex] != "." and i == 8 and deadEndCount == len(startingVals) ):

         print(f"\n All possible orders of values for this column have been found...\n Checking if more than 2... There are", pColOrderCount )

         if (len(possibleColOrder) > 1):

            print(f"\n So column: {bigColIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go and try another row, column, or box...")

            skipCols.append(bigColIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

            temp_col_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
            board = copy.deepcopy(board_backup)

            findEasiestStart(board, skipRows, skipCols, skipBoxes)

         elif (len(possibleColOrder) == 1):
            #if column only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
            for z in range(9):

               board[z][bigColIndex] = possibleColOrder[0][z] #re save only solution to board before sending the board with the completed col to next start

            print(f"\n Column completed with only possible combination! Sending board to next starting point...\n New Board Being Sent: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            findEasiestStart(board, skipRows, skipCols, skipBoxes)

      #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, AND THE DEADENDCOUNT IS MAXXED BEFORE FINISHING ROW
      elif (deadEnd == True and i <= 8 and deadEndCount == len(startingVals) ):

         print(f"\n All possible orders of values for this col have been tried...\n Checking how many possible... There are", pColOrderCount)

         if (pColOrderCount > 1):

            print(f"\n So Col: {bigColIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

            skipCols.append(bigColIndex) #add this Col to list of Cols for easiestStart func to skip when choosing starting position

            temp_col_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
            board = copy.deepcopy(board_backup)

            findEasiestStart(board, skipRows, skipCols, skipBoxes)

         elif (pColOrderCount == 1):

            #if Col only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
            for q in range(9):

               board[q][bigColIndex] = possibleColOrder[0][q] #re save only solution to board before sending the board with the completed Col to next start

            print(f"\n Col completed with only possible combination after checking every single combo! Sending board to next starting point...\n New Board Being Sent: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

            findEasiestStart(board, skipRows, skipCols, skipBoxes)

         elif (pColOrderCount < 1):

            print(f"\n Sorry, no possible combinations found for col {bigColIndex} after trying all possible permutations and reaching a dead end before the end of said col,\n while the end of the row contains a '.' still...\n")
            return possibleColOrder

                  
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
   print("\n", findEasiestStart(board2, [], [], [])) #send board2 to validity checker func to return if it is valid or not

   


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
   print("\n", findEasiestStart(board3, [], [], [])) #send board3 to validity checker func to return if it is valid or not

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
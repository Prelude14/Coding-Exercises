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

import findEasiestStart

import sudokuSolveRow

import sudokuSolveBox

import sudokuResetSkips


"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveCol(board: list[list[str]], bigColIndex, startingVals, deadEndCount, possibleColOrder, pColOrderCount, skippedVals) -> []:

   temp_col_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   tempPossibleCol = [  ]
   newSkippedVals = [] #makes sure each solver function starts with empty list before skips are reset
   
   print("\n Starting Values at beginning of SolveCol:",startingVals[deadEndCount],", Possible Permutations:",len(startingVals),", DeadEndCount:",deadEndCount, "\n")

   for i in range(9): #look through board until first period is found

      newColValWorks = False #define this value as false every time a new value is checked
      deadEnd = False #if deadEnd is found, then stop trying current order of values

      if (board[i][bigColIndex] == "."): #find every period in the col sent to be solved

         while (newColValWorks == False and deadEnd == False and deadEndCount != len(startingVals) ): 
         #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

            for index, x in enumerate(startingVals[deadEndCount]):

               temp_col_board[i][bigColIndex] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

               tColBoardIsValid = validityChecker.validityChecker(temp_col_board) #pass temp board once so that it doesnt run every if statement below

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

                     sudokuSolveCol(board, bigColIndex, startingVals, deadEndCount, possibleColOrder, pColOrderCount, skippedVals) #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list

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
            allOrders = sudokuSolveCol(board, bigColIndex, startingVals, deadEndCount, possibleColOrder, pColOrderCount, skippedVals) 

            print("\n After saving possible col order",pColOrderCount,"we have checked the rest of the startingvals and finished with ", len(allOrders), "possible orders...")

         elif (deadEndCount == len(startingVals) ): #if we have no more permutations to check after attempting to save the last possible order, we need to decide to fill the board or not

            print("\n So the column has finished checking every possible combination, it found", pColOrderCount, "possible column order(s)...")

            print(f"\n PossibleColOrder: {possibleColOrder}")

            if (pColOrderCount > 1):

               print(f"\n So column {bigColIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

               skippedVals[1].append(bigColIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

               temp_col_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
               board = copy.deepcopy(board_backup)

               findEasiestStart.findEasiestStart(board, skippedVals)

            elif (pColOrderCount == 1):
               #if column only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
               for y in range(9):

                  board[y][bigColIndex] = possibleColOrder[0][y] #re save only solution to board before sending the board with the completed col to next start


               print(f"\n Column completed with only possible combination! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
               pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
               newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

               findEasiestStart.findEasiestStart(board, newSkippedVals)

      #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleColOrder list, 
      elif (board[i][bigColIndex] != "." and i == 8 and deadEndCount == len(startingVals) ):

         print(f"\n All possible orders of values for this column have been found...\n Checking if more than 2... There are", pColOrderCount )

         if (len(possibleColOrder) > 1):

            print(f"\n So column: {bigColIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go and try another row, column, or box...")

            skippedVals[1].append(bigColIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

            temp_col_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
            board = copy.deepcopy(board_backup)

            findEasiestStart.findEasiestStart(board, skippedVals)

         elif (len(possibleColOrder) == 1):
            #if column only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
            for z in range(9):

               board[z][bigColIndex] = possibleColOrder[0][z] #re save only solution to board before sending the board with the completed col to next start

            print(f"\n Column completed with only possible combination! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
            newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

            findEasiestStart.findEasiestStart(board, newSkippedVals)

      #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, AND THE DEADENDCOUNT IS MAXXED BEFORE FINISHING ROW
      elif (deadEnd == True and i <= 8 and deadEndCount == len(startingVals) ):

         print(f"\n All possible orders of values for this col have been tried...\n Checking how many possible... There are", pColOrderCount)

         if (pColOrderCount > 1):

            print(f"\n So Col: {bigColIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

            skippedVals[1].append(bigColIndex) #add this Col to list of Cols for easiestStart func to skip when choosing starting position

            temp_col_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
            board = copy.deepcopy(board_backup)

            findEasiestStart.findEasiestStart(board, skippedVals)

         elif (pColOrderCount == 1):

            #if Col only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
            for q in range(9):

               board[q][bigColIndex] = possibleColOrder[0][q] #re save only solution to board before sending the board with the completed Col to next start

            print(f"\n Col completed with only possible combination after checking every single combo! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
            newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

            findEasiestStart.findEasiestStart(board, newSkippedVals)

         elif (pColOrderCount < 1):

            print(f"\n Sorry, no possible combinations found for col {bigColIndex} after trying all possible permutations and reaching a dead end before the end of said col,\n while the end of the row contains a '.' still...\n")
            return possibleColOrder

                  
   #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.


def main():
   print("=" * 50)
   print(" Sudoku Solve Col Function:")
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
   #print("\n", findEasiestStart(boardHARDMODE, [], [], []))
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






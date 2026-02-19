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

import sudokuSolveCol

import sudokuSolveBox

import sudokuResetSkips


"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveRow(board: list[list[str]], bigRowIndex, startingVals, deadEndCount, possibleRowOrder, pRowOrderCount, skippedVals) -> []:

   temp_row_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   tempPossibleRow = [ ]
   newSkippedVals = [] #makes sure each solver function starts with empty list before skips are reset

   print("\n Starting Values at beginning of SolveRow: ",startingVals[deadEndCount],", Possible Permutations:",len(startingVals),", DeadEndCount:",deadEndCount, "\n")

   for j in range(9): #look through board until first period is found

      newRowValWorks = False #define this value as false every time a new value is checked
      deadEnd = False #if deadEnd is found, then stop trying current order of values

      if (board[bigRowIndex][j] == "."): #find every period in the row sent to be solved

         while (newRowValWorks == False and deadEnd == False and deadEndCount != len(startingVals) ): 
         #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

            for index, x in enumerate(startingVals[deadEndCount]): #only check each values in one set of values at a time, index by 

               temp_row_board[bigRowIndex][j] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

               tRowBoardIsValid = validityChecker.validityChecker(temp_row_board) #pass temp board once so that it doesnt run every if statement below

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
                     possibleRowOrder = sudokuSolveRow(board, bigRowIndex, startingVals, deadEndCount, possibleRowOrder, pRowOrderCount, skippedVals)

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
            print(f" PossibleRowOrder: {possibleRowOrder}\n pOrderCount: {pRowOrderCount}")

         board = copy.deepcopy(board_backup) #re write regular board back to starting point to try different order of numbers again
         
         #we should increment deadEndCount in order to check the next possible order of vals, otherwise it infintely checks just the first correct order
         deadEndCount += 1

         if (deadEndCount != len(startingVals) ): #check to see if we tried all permutations of startingVals yet

            print(f"\n So we finished checking and potentially saving a row's solution while there is still more startingVals to try,\n checking if there is now more than 1 possible solution...")

            if (pRowOrderCount <= 1): #if we have saved up to one unique solution so far
               
               print(f"\n So there is either 0 or 1 unique possible solution curently saved... Will need to continue checking combos...")
               print(f"\n Checking next possible combination by sending updated deadEndCount({deadEndCount}) to SolveRow recursively...")
               #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
               allOrders = sudokuSolveRow(board, bigRowIndex, startingVals, deadEndCount, possibleRowOrder, pRowOrderCount, skippedVals)

               print("\n After saving possible row order",pRowOrderCount,", we have checked the rest of the startingvals and finished with", len(allOrders), "possible orders...")

               return allOrders #need to return the list of possible rows after 

            elif (pRowOrderCount > 1): #if we have now saved 2 unique solutions AND DEADEND NOT HIT YET, we want to skip early to avoid doing 720 permutations

               print(f"\n So this row now has more than 1 unique possible solution curently saved...\n Skip this row (row {bigRowIndex}) and move on...")
               print(f"\n pRowOrderCount: {pRowOrderCount}, PossibleRowOrder: {possibleRowOrder}")

               skippedVals[0].append(bigRowIndex) #add index of this row to list of rows for easiestStart func to skip when choosing starting position

               temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different order of numbers again
               board = copy.deepcopy(board_backup)

               findEasiestStart.findEasiestStart(board, skippedVals)


         elif (deadEndCount == len(startingVals) ): #if we have reached end of possible permutations of startingVals

            print("\n So the row has finished checking every possible combination, it found", pRowOrderCount, "possible row order(s)...")

            print(f"\n PossibleRowOrder: {possibleRowOrder}")

            if (pRowOrderCount > 1):

               print(f"\n So row {bigRowIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")


               skippedVals[0].append(bigRowIndex) #add index of this row to list of rows for easiestStart func to skip when choosing starting position

               temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different order of numbers again
               board = copy.deepcopy(board_backup)

               findEasiestStart.findEasiestStart(board, skippedVals)

            elif (pRowOrderCount == 1):

               #if row only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
               for y in range(9):

                  board[bigRowIndex][y] = possibleRowOrder[0][y] #re save only solution to board before sending the board with the completed row to next start

               print(f"\n Row completed with only possible combination! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
               pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
               newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

               findEasiestStart.findEasiestStart(board, newSkippedVals)


      #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, 
      elif (board[bigRowIndex][j] != "." and j == 8 and deadEndCount == len(startingVals) ):

         print(f"\n All possible orders of values for this row have been found...\n Checking if more than 2... There are", pRowOrderCount)

         if (pRowOrderCount > 1):

            print(f"\n So row: {bigRowIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

            skippedVals[0].append(bigRowIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

            temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
            board = copy.deepcopy(board_backup)

            findEasiestStart.findEasiestStart(board, skippedVals)

         elif (pRowOrderCount == 1):

            #if row only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
            for z in range(9):

               board[bigRowIndex][z] = possibleRowOrder[0][z] #re save only solution to board before sending the board with the completed row to next start

            print(f"\n Row completed with only possible combination! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
            newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

            findEasiestStart.findEasiestStart(board, newSkippedVals)

      #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, AND THE DEADENDCOUNT IS MAXXED BEFORE FINISHING ROW
      elif (deadEnd == True and j <= 8 and deadEndCount == len(startingVals) ):

         print(f"\n All possible orders of values for this row have been tried...\n Checking how many possible... There are", pRowOrderCount)

         if (pRowOrderCount > 1):

            print(f"\n So row: {bigRowIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

            skippedVals[0].append(bigRowIndex) #add this row to list of rows for easiestStart func to skip when choosing starting position

            temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
            board = copy.deepcopy(board_backup)

            findEasiestStart.findEasiestStart(board, skippedVals)

         elif (pRowOrderCount == 1):

            #if row only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
            for q in range(9):

               board[bigRowIndex][q] = possibleRowOrder[0][q] #re save only solution to board before sending the board with the completed row to next start

            print(f"\n Row completed with only possible combination after checking every single combo! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
            pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
            newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

            findEasiestStart.findEasiestStart(board, newSkippedVals)

         elif (pRowOrderCount < 1):

            print(f"\n Sorry, no possible combinations found for row {bigRowIndex} after trying all possible permutations and reaching a dead end before the end of said row,\n while the end of the row contains a '.' still...\n")
            return possibleRowOrder

   #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.


def main():
   print("=" * 50)
   print(" Sudoku Solve Row Function:")
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
   #print("\n", sudokuSolveRow(boardHARDMODE, [], [], []))
   #print("\n", validityChecker(board1)) #send board1 to validity checker func to return if it is valid or not

   
if __name__ == "__main__":
   main()



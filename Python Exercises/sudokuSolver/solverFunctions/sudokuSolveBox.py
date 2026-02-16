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

import sudokuSolveCol

"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveBox(board: list[list[str]], bigBoxIndex, startingVals, deadEndCount, possibleBoxOrder, pBoxOrderCount, skipRows, skipCols, skipBoxes) -> []:

   temp_box_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   tempPossibleBox = [ ]

   print("\n Starting Values at beginning of SolveBox: ",startingVals[deadEndCount], "DeadEndCount:",deadEndCount, "\n")

   for m in range(3): #look through box until first period is found

      for n in range(3): 

         newBoxValWorks = False #define this value as false every time a new value is checked
         deadEnd = False #if deadEnd is found, then stop trying current order of values
         box_MIndex = 0 #define early so can use later
         box_NIndex = 0 #define early so can use later

         if (bigBoxIndex == 0 or bigBoxIndex == 3 or bigBoxIndex == 6):

            box_MIndex = bigBoxIndex + m #need coordinates to start at (0,0), (3,0), or (6,0)

            if (board[box_MIndex][n] == "."): #find every period in the box sent to be solved

               while (newBoxValWorks == False and deadEnd == False and deadEndCount != len(startingVals)): 
               #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

                  for index, x in enumerate(startingVals[deadEndCount]): #only check each values in one set of values at a time, index by 

                     temp_box_board[box_MIndex][n] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

                     tBoxBoardIsValid = validityChecker.validityChecker(temp_box_board) #pass temp board once so that it doesnt run every if statement below

                     if (tBoxBoardIsValid == True):
                        #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                        board[box_MIndex][n] = str(x) #actually change board and then trigger while loop to end
                        #pprint.pprint(temp_board)
                        pprint.pprint(board)
                        newBoxValWorks = True
                        break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on
                        #Started fixing up to here+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                     elif (tBoxBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and m != 2):

                        deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, dead end reached at box {box_MIndex}, col {n}, exiting loop and attempting to try next combo...\n Final Board: \n")
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
   print(" Sudoku Solve Box Function:")
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





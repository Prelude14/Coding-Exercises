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

                  print(f" Duplicate value in ROW, at row {i} and col {j}, where val = {val}, and row[{x}]: {row[x]}" )

                  return False

            #COL CHECK val against every other value inside same col for duplicates ========================================================================================== COL
            #so we use from val's i index+1 to end of the col, since once a val is checked and cleared at index i, we wont need to check the same index again
            for y in range(i+1, len(board)):
            
               if (val == board[y][j]):

                  print(f" Duplicate value in COL, at row {i} and col {j}, where val = {val}, and board[{y}][{j}]: {board[y][j]}" )

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

                  print(f"\n Duplicate value in SUB-BOX, at BOX: {m} and item: {n}, where val = {item}, and box[{n}][{p}] = {box[p]}" )

                  return False
   
   #if the entire board matrix is gone through and no duplicates were found, return true      
   return True   


def main():
   print("=" * 50)
   print(" Valid Sudoku CHECKER")
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

      board2 = [["8","3",".",".","7",".",".",".","."]
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
   print("\n", validityChecker(boardHARDMODE)) #send board1 to validity checker func to return if it is valid or not


   
if __name__ == "__main__":
   main()







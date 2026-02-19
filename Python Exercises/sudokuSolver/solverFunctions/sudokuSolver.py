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


def main():
   print("=" * 50)
   print(" Valid Sudoku Solver")
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
      
      #This is the difficult sudoku board I found in a video about sudoku tips anmd wanted to try in the solver, unfortunately because there is only 3 filled in vals at most per row, col or box,
      #The solver can't figure out the board, since there are too many possible solutions to each row, col, or box. This means it checks all 720 different permutations of the remaining 6 values for 
      #row, col, or box, which crashes python by itself since it hits a recursion limit, but even if it didn't do that, I'm pretty sure it would just end up getting at least more than one possible 
      #solution for every row, col or box, and that would lead it to eventually skip over every single row, col or box in the board when considering the first place to solve, and returning an unchanged
      #board
      boardHMSTART = [["5","4",".",".","8",".",".",".","."]
                     ,["9",".",".",".",".",".",".",".","."]
                     ,[".",".",".","2",".",".","3",".","."]
                     ,[".",".","1","6",".",".",".",".","."]
                     ,["8",".",".",".","9",".",".",".","5"]
                     ,[".",".",".",".",".","3","7",".","."]
                     ,[".",".","6",".",".","7",".",".","."]
                     ,[".",".",".",".",".",".",".",".","1"]
                     ,[".",".",".",".","5",".",".","9","4"]]
      
      #This version is able to be solved by the solver because enough values are filled in
      boardHARDMODE = [["5","4",".","9","8","6","1","2","7"] 
                      ,["9",".","2",".","3",".",".",".","."]
                      ,[".",".",".","2",".",".","3",".","."]
                      ,[".",".","1","6","2",".",".",".","."]
                      ,["8","3","4","7","9",".","2",".","5"]
                      ,[".",".","9",".","4","3","7",".","."]
                      ,[".",".","6",".",".","7",".",".","."]
                      ,[".",".","5",".","6",".",".",".","1"]
                      ,["1",".",".",".","5","2",".","9","4"]]
   
      #This is a copy of the properly filled out solution of the hard mode board, used to compare final results or troubleshoot the solver in progress
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
   #hard partially filled board that causes the program to crash due to too many possibilties to check (at most there is only 3 filled values in any row, col or box to start, so 
   #it has to check all 720 possible permutations of the remaining 6 values), which leads to too many recursive calls to the function, so python closes it automatically before it finishes
   boardHMSTART = [["5","4",".","9","8",".",".",".","."]
                  ,["9",".",".","1",".",".",".",".","."]
                  ,[".",".",".","2",".",".","3",".","."]
                  ,[".",".","1","6",".","8","9",".","."]
                  ,["8",".",".",".","9",".","2",".","5"]
                  ,[".",".",".",".",".","3","7","1","8"]
                  ,[".",".","6",".",".","7",".","3","."]
                  ,[".",".",".",".",".",".",".","7","1"]
                  ,[".",".",".",".","5",".",".","9","4"]]

   #same hard board, but I filled in more missing parts in order to find the point where it can be solved, and this board currently works actually, I've even checked it with the solution above
   boardHARDMODE = [["5","4",".","9","8","6","1","2","7"]
                   ,["9",".","2",".","3",".",".",".","."]
                   ,[".",".",".","2",".",".","3",".","."]
                   ,[".",".","1","6","2",".",".",".","."]
                   ,["8","3","4","7","9",".","2",".","5"]
                   ,[".",".","9",".","4","3","7",".","."]
                   ,[".",".","6",".",".","7",".",".","."]
                   ,[".",".","5",".","6",".",".",".","1"]
                   ,["1",".",".",".","5","2",".","9","4"]]

   print("\n Input Hard Mode Starting Board: ") #print board1 to console,
   pprint.pprint(boardHMSTART)
   #pprint.pprint(boardHARDMODE)
   print("-" * 50)

   print("\n Output:") #print output of validity of board1
   print("-" * 50)
   print("\n", findEasiestStart.findEasiestStart(boardHMSTART, [ [], [], [] ]) )
   #print("\n", findEasiestStart.findEasiestStart(boardHARDMODE, [[], [], []]) )
   #print("\n", validityChecker.validityChecker(board1)) #send board1 to validity checker func to return if it is valid or not


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





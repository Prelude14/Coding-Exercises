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

import sudokuResetSkips

"""Function to attempt solving partially completed sudoku board, given list of 9 other lists of 9 ints or ".", as well as the index of the row with the most filled cells in the board already"""
def sudokuSolveBox(board: list[list[str]], bigBoxIndex, startingVals, deadEndCount, possibleBoxOrder, pBoxOrderCount, skippedVals) -> []:

   temp_box_board = copy.deepcopy(board) #create copy of board in order to edit cells in only if they work
   board_backup = copy.deepcopy(board) #create copy of board in order to go back to if deadend is reached

   tempPossibleBox = [ ]
   newSkippedVals = [] #makes sure each solver function starts with empty list before skips are reset

   print("\n Starting Values at beginning of SolveBox: ",startingVals[deadEndCount], ", Possible Permutations: ",len(startingVals), ", DeadEndCount:",deadEndCount, "\n")

   for m in range(3): #look through box until first period is found

      for n in range(3): 

         newBoxValWorks = False #define this value as false every time a new value is checked
         deadEnd = False #if deadEnd is found, then stop trying current order of values
         box_MIndex = 0 #define early so can use later
         box_NIndex = 0 #define early so can use later

         if (bigBoxIndex == 0 or bigBoxIndex == 3 or bigBoxIndex == 6):

            box_MIndex = bigBoxIndex + m #need coordinates to start at (0,0), (3,0), or (6,0)

            if (board[box_MIndex][n] == "."): #find every period in the box sent to be solved

               while (newBoxValWorks == False and deadEnd == False and deadEndCount != len(startingVals) ): 
               #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

                  for index, x in enumerate(startingVals[deadEndCount]): #only check each values in one set of values at a time, index by 

                     temp_box_board[box_MIndex][n] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

                     tBoxBoardIsValid = validityChecker.validityChecker(temp_box_board) #pass temp board once so that it doesnt run every if statement below

                     #print(f"\n Box 0, 3, or 6, m = {m}, n= {n}, index = {index}, (len(startingVals[deadEndCount])-1) = {(len(startingVals[deadEndCount])-1)}, isValid = {tBoxBoardIsValid}")

                     if (tBoxBoardIsValid == True):
                        #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                        board[box_MIndex][n] = str(x) #actually change board and then trigger while loop to end
                        #pprint.pprint(temp_board)
                        pprint.pprint(board)
                        newBoxValWorks = True
                        break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

                     elif (tBoxBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and m <= 2 and n <= 2):

                        deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, dead end reached at box {bigBoxIndex}, row {box_MIndex}, col {n}, exiting loop and attempting to try next combo...\n Dead End Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                        board = copy.deepcopy(board_backup)
                        #newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the row

                        deadEndCount += 1

                        if (deadEndCount <= (len(startingVals)-1)):  #if we still have other combos to try, increment deadEndCount and move on to next combo
                           print(" Starting Values: ",startingVals[deadEndCount-1], "\n New Starting Values: ", startingVals[deadEndCount], "\n")

                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                           #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
                           possibleBoxOrder = sudokuSolveBox(board, bigBoxIndex, startingVals, deadEndCount, possibleBoxOrder, pBoxOrderCount, skippedVals)

                           return possibleBoxOrder #exit function after returning from recursive solveBox call, so that it doesn't try any more values after dead end is reached

                        elif (deadEndCount > (len(startingVals)-1) and pBoxOrderCount == 0): #if we finish trying a combo before we get to the last item in the row, and we are out of combos
                           #if we have tried the last value in the last combo of values, and we have 0 possible solutions, we need to quit since we have run out of possible combinations to try
                           print("\n Sorry! We have tried every possible combination of values on box ", bigBoxIndex, ".\n This means the board is not solvable, or that we made a mistake somewhere...\n")
                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )
                           print("\n Exiting Function...")
                           return possibleBoxOrder #exit function without calling solveBox again, since we have reached a full deadend without any solutions

                        elif (deadEndCount > (len(startingVals)-1) and pBoxOrderCount > 0): #if we finish trying a combo before we get to the last item in the Box, and we are out of combos (m!=2)
                           #AND we have more than one possible solution, we need to properly return said list of solutions
                           print("\n We have now tried every possible combination of values on Box", bigBoxIndex, "\n")
                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                           break 
                           #if deadendCount maxed but we have solutions, we need to break from this for loop, which will break while loop, and then on the last check of m and n with full deadEndCount, 
                           #we will pick a combo. NOTE: if deadEndCount max hit before j is through entire row and the row ends in an empty cell, the ifs that this will go to won't work, since
                           #they need the last item in the row to be a actual number and not a "."

                     elif (tBoxBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and m == 2  and n == 2 and deadEndCount == len(startingVals) ):

                        noSolutionFound = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, no solution found for the box {bigBoxIndex}, exiting program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        return possibleBoxOrder

                  #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

               if (deadEndCount == len(startingVals) and pBoxOrderCount == 0):

                  noSolutionFound = True #if we tried all possible combinations of the values avaliable, and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, no solution found for the row {bigRowIndex}, deadEndCount = {deadEndCount}, and startingVals Length = {len(startingVals)}, exiting program...\n Final Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  return possibleBoxOrder


            #AFTER WHILE LOOP AND X FOR LOOP ENDS, BUT STILL WITHIN N FOR and then M FOR, need to create list containing the valid order that was found and store it in big list containing all 
            #possible orders for this box, should only run on final lap of for loops since m == 2 and n == 2 , and only when dead end count is not full
            #if end of box and end of possible inputs is reached, and board is valid, then box must be correct, so add it to possible orders, and then if deadEndCount is still less than 
            #startingVals length, it means there is still combos to try, so we need to save the Box's order and then try the other options
            if (board[box_MIndex][n] != "." and m == 2  and n == 2 and deadEndCount != len(startingVals) ):
               print(f"\n Possible Box Order Found! Saving order to possibleBoxOrder...\n Box Being Saved: {bigBoxIndex}")

               for a in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                  #this way when MIndex = 2 (BBindex + m == 0 + 2), MIndex-a = 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 0 = board[0-2][0-2]
                  #or when MIndex = 5 (BBindex + m == 3 + 2), MIndex-a = 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 3 = board[3-5][0-2]
                  #or when MIndex = 8 (BBindex + m == 6 + 2), MIndex-a 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 6 = board[6-8][0-2]
                  for b in range(3): 
                     #n just needs to be 0-2 for each of the current 3 boxes (0, 3, and 6)

                     tempPossibleBox.append(board[(box_MIndex-a)][b]) #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list

               if tempPossibleBox not in possibleBoxOrder: #we only want to add possible Box order if it is different than the rest of already saved possible orders
                  possibleBoxOrder.append(tempPossibleBox) #add temp list to end of big list

                  pBoxOrderCount += 1 
                  #after adding the UNIQUE completed Box order to the list, we need to increment this so next time a possible order is found in the next call to this function, it can be added properly
                  print(f" Unique solution found...tempPossibleBox: {tempPossibleBox}\n PossibleBoxOrder: {possibleBoxOrder}\n pOrderCount: {pBoxOrderCount}")

               elif tempPossibleBox in possibleBoxOrder:

                  print("\n Oh! It looks like that possible order has already been saved to the list, so we aren't saving it, moving on... ")
                  print(f" PossibleBoxOrder: {possibleBoxOrder}\n pOrderCount: {pBoxOrderCount}")

               board = copy.deepcopy(board_backup) #re write regular board back to starting point to try different order of numbers again
         
               #we should increment deadEndCount in order to check the next possible order of vals, otherwise it infintely checks just the first correct order
               deadEndCount += 1

               if (deadEndCount != len(startingVals) ):
                  print(f"\n Checking next possible combination by sending updated deadEndCount({deadEndCount}) to SolveBox recursively...")
                  #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
                  allOrders = sudokuSolveBox(board, bigBoxIndex, startingVals, deadEndCount, possibleBoxOrder, pBoxOrderCount, skippedVals)

                  print("\n After saving possible Box order",pBoxOrderCount,", we have checked the rest of the startingvals and finished with", len(allOrders), "possible orders...")

                  return allOrders #need to return the list of possible Boxes after 

               elif (deadEndCount == len(startingVals) ):

                  print("\n So the Box has finished checking every possible combination, it found", pBoxOrderCount, "possible Box order(s)...")

                  print(f"\n PossibleBoxOrder: {possibleBoxOrder}")

                  if (pBoxOrderCount > 1):

                     print(f"\n So Box {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                     skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                     temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different order of numbers again
                     board = copy.deepcopy(board_backup)

                     findEasiestStart.findEasiestStart(board, skippedVals)

                  elif (pBoxOrderCount == 1):

                     #if Box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                     #re save only solution to board before sending the board with the completed box to next start
                     
                     counterA = 0 #set up seperate variable from a, to access all 9 vals in possibleOrder while using a to index the overall board properly 
                     #cA =0 results in possibleOrder[0][0+ (0)] = [0][0], then [0][1 - (0)]= [0][1], then [0][2], then cA is 1 results in [0][0+ (3)] = [0][3], [0][4], [0][5]
                     #then cA = 2 resulting in [0][0+6)] = [0][6], [0][7], [0][8]
                     for a in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                        #this way when MIndex = 2 (BBindex + m == 0 + 2), MIndex-a = 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 0 = board[0-2][0-2]
                        #or when MIndex = 5 (BBindex + m == 3 + 2), MIndex-a = 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 3 = board[3-5][0-2]
                        #or when MIndex = 8 (BBindex + m == 6 + 2), MIndex-a 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 6 = board[6-8][0-2]
                        
                        for b in range(3): 
                           #n just needs to be 0-2 for each of the current 3 boxes (0, 3, and 6)

                           #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                           board[(box_MIndex-a)][b] = possibleBoxOrder[0][b+(counterA*3)] 

                           #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list
                        counterA +=1

                     print(f"\n Box completed with only possible combination! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
                     pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                     newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                     findEasiestStart.findEasiestStart(board, newSkippedVals)

            #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleBoxOrder list, 
            elif (board[box_MIndex][box_NIndex] != "." and m == 2 and n == 2 and deadEndCount == len(startingVals) ):

               print(f"\n All possible orders of values for this box have been found...\n Checking if more than 2... There are", pBoxOrderCount)

               if (pBoxOrderCount > 1):

                  print(f"\n So Box: {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                  skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                  temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
                  board = copy.deepcopy(board_backup)

                  findEasiestStart.findEasiestStart(board, skippedVals)

               elif (pBoxOrderCount == 1):

                  #if box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                  #re save only solution to board before sending the board with the completed box to next start
                     
                  counterB = 0 #set up seperate variable from c to access all 9 vals in possibleOrder while using c to index the overall board properly 
                  #cB =0 results in possibleOrder[0][0+ (0)] = [0][0], then [0][1 - (0)]= [0][1], then [0][2], then cB is 1 results in [0][0+ (3)] = [0][3], [0][4], [0][5]
                  #then cB = 2 resulting in [0][0+6)] = [0][6], [0][7], [0][8] 
                  for c in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                     #this way when MIndex = 2 (BBindex + m == 0 + 2), MIndex-a = 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 0 = board[0-2][0-2]
                     #or when MIndex = 5 (BBindex + m == 3 + 2), MIndex-a = 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 3 = board[3-5][0-2]
                     #or when MIndex = 8 (BBindex + m == 6 + 2), MIndex-a 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 6 = board[6-8][0-2]
                        
                     for d in range(3): 
                        #n just needs to be 0-2 for each of the current 3 boxes (0, 3, and 6)

                        #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                        board[(box_MIndex-c)][d] = possibleBoxOrder[0][d+(counterB*3)] 

                        #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list
                     counterB +=1

                  print(f"\n Box completed with only possible combination! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                  newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                  findEasiestStart.findEasiestStart(board, newSkippedVals)


            #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, AND THE DEADENDCOUNT IS MAXXED BEFORE FINISHING ROW
            elif (deadEnd == True and m <= 2 and n <= 2 and deadEndCount == len(startingVals) ):

               print(f"\n All possible orders of values for this box have been tried...\n Checking how many possible... There are", pBoxOrderCount)

               if (pBoxOrderCount > 1):

                  print(f"\n So Box: {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                  skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                  temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
                  board = copy.deepcopy(board_backup)

                  findEasiestStart.findEasiestStart(board, skippedVals)

               elif (pBoxOrderCount == 1):

                  #if Box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                  #re save only solution to board before sending the board with the completed box to next start

                  rowIndexStart = bigBoxIndex #need to force rowIndex to start with 0, 3 or 6
                  rowIndexEnd = rowIndexStart+3 #need rowIndex to make range end at either 2, 5 or 8 (before 3, 6 or 9)
                     
                  counterC = 0 #set up seperate variable from e to access all 9 vals in possibleOrder while using e to index the overall board properly 
                  #cC =0 results in possibleOrder[0][0+ (0)] = [0][0], then [0][1 - (0)]= [0][1], then [0][2], then cC is 1 results in [0][0+ (3)] = [0][3], [0][4], [0][5]
                  #then cC = 2 resulting in [0][0+6)] = [0][6], [0][7], [0][8]
                  for e in range(rowIndexStart, rowIndexEnd): #CANT USE MIndex to find index (we don't know what m or n is exactly), need to use bigBoxIndex instead
                        
                     for f in range(3): 
                        #n just needs to be 0-2 for each of the current 3 boxes (0, 3, and 6)

                        #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                        board[(e)][f] = possibleBoxOrder[0][f+(counterC*3)] 

                        #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list
                     counterC +=1

                  print(f"\n Box {bigBoxIndex} completed with only possible combination after checking every single combo! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                  newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                  findEasiestStart.findEasiestStart(board, newSkippedVals)

               elif (pBoxOrderCount < 1):

                  print(f"\n Sorry, no possible combinations found for Box {bigBoxIndex} after trying all possible permutations and reaching a dead end before the end of said Box,\n while the end of the Box contains a '.' still...\n")
                  return possibleRowOrder

         #========================================== END BOX 0, 3 and 6 solves ==========================================================================================================================

         elif (bigBoxIndex == 1 or bigBoxIndex == 4 or bigBoxIndex == 7):

            box_MIndex = m + (bigBoxIndex - 1) #need coordinates to start at (0,3), (3,3), or (6,3)
            box_NIndex = 3 + n #need coordinates to start at (0,3), (3,3), or (6,3)

            if (board[box_MIndex][box_NIndex] == "."): #find every period in the box sent to be solved

               while (newBoxValWorks == False and deadEnd == False and deadEndCount != len(startingVals) ): 
               #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

                  for index, x in enumerate(startingVals[deadEndCount]): #only check each values in one set of values at a time, index by the deadEndCount

                     temp_box_board[box_MIndex][box_NIndex] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

                     tBoxBoardIsValid = validityChecker.validityChecker(temp_box_board) #pass temp board once so that it doesnt run every if statement below

                     #print(f"\n Box 1, 4, or 7, m = {m}, n= {n}, index = {index}, (len(startingVals[deadEndCount])-1) = {(len(startingVals[deadEndCount])-1)}, isValid = {tBoxBoardIsValid}")

                     if (tBoxBoardIsValid == True):
                        #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                        board[box_MIndex][box_NIndex] = str(x) #actually change board and then trigger while loop to end
                        #pprint.pprint(temp_board)
                        pprint.pprint(board)
                        newBoxValWorks = True
                        break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

                     elif (tBoxBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and m <= 2 and n <=2): 

                        deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, dead end reached at box {bigBoxIndex}, row {box_MIndex}, col {box_NIndex}, exiting loop and attempting to try next combo...\n Dead End Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                        board = copy.deepcopy(board_backup)
                        #newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the row

                        deadEndCount += 1

                        if (deadEndCount <= (len(startingVals)-1)):  #if we still have other combos to try, increment deadEndCount and move on to next combo
                           print(" Starting Values: ",startingVals[deadEndCount-1], "\n New Starting Values: ", startingVals[deadEndCount], "\n")

                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                           #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
                           possibleBoxOrder = sudokuSolveBox(board, bigBoxIndex, startingVals, deadEndCount, possibleBoxOrder, pBoxOrderCount, skippedVals ) 

                           return possibleBoxOrder #exit function after returning from recursive solveBox call, so that it doesn't try any more values after dead end is reached

                        elif (deadEndCount > (len(startingVals)-1) and pBoxOrderCount == 0): #if we finish trying a combo before we get to the last item in the row, and we are out of combos
                           #if we have tried the last value in the last combo of values, and we have 0 possible solutions, we need to quit since we have run out of possible combinations to try
                           print("\n Sorry! We have tried every possible combination of values on box ", bigBoxIndex, ".\n This means the board is not solvable, or that we made a mistake somewhere...\n")
                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )
                           print("\n Exiting Function...")
                           return possibleBoxOrder #exit function without calling solveBox again, since we have reached a full deadend without any solutions

                        elif (deadEndCount > (len(startingVals)-1) and pBoxOrderCount > 0): #if we finish trying a combo before we get to the last item in the Box, and we are out of combos (m!=2)
                           #AND we have more than one possible solution, we need to properly return said list of solutions
                           print("\n We have now tried every possible combination of values on Box", bigBoxIndex, "\n")
                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                           break 
                           #if deadendCount maxed but we have solutions, we need to break from this for loop, which will break while loop, and then on the last check of m and n with full deadEndCount, 
                           #we will pick a combo. NOTE: if deadEndCount max hit before m and n is through entire box and the box ends in an empty cell, the ifs that this will go to won't work, since
                           #they need the last item in the box to be a actual number and not a "."

                     elif (tBoxBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and m == 2  and n == 2 and deadEndCount == len(startingVals) ):

                        noSolutionFound = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, no solution found for the box {bigBoxIndex}, exiting program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        return possibleBoxOrder

                  #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

               if (deadEndCount == len(startingVals) and pBoxOrderCount == 0): #if no more orders of startingVals to try and no possible orders found

                  noSolutionFound = True #if we tried all possible combinations of the values avaliable, and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, no solution found for the row {bigRowIndex}, deadEndCount = {deadEndCount}, and startingVals Length = {len(startingVals)}, exiting program...\n Final Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  return possibleBoxOrder

            #AFTER WHILE LOOP AND X FOR LOOP ENDS, BUT STILL WITHIN N FOR and then M FOR, need to create list containing the valid order that was found and store it in big list containing all 
            #possible orders for this box, should only run on final lap of for loops since m == 2 and n == 2 , and only when dead end count is not full
            #if end of box and end of possible inputs is reached, and board is valid, then box must be correct, so add it to possible orders, and then if deadEndCount is still less than 
            #startingVals length, it means there is still combos to try, so we need to save the Box's order and then try the other options
            if (board[box_MIndex][box_NIndex] != "." and m == 2 and n == 2 and deadEndCount != len(startingVals) ):
               print(f"\n Possible Box Order Found! Saving order to possibleBoxOrder...\n Box Being Saved: {bigBoxIndex}")

               for a in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                  #this way when MIndex = 2 ((BBindex = 1, and then -1, so 1-1=0) + m which is 2), we get 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 1 = board[0-2][3-5]
                  #or when MIndex = 5 ((BBindex = 4, and then -1, so 4-1=3)+ m which is 2), we get 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 4 = board[3-5][3-5]
                  #or when MIndex = 8 ((BBindex = 7, and then -1, so 7-1=6)+ m which is 2), we get 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 7 = board[6-8][3-5]
                  for b in range(3,6):
                     #n index just needs to be 3,4 and 5

                     tempPossibleBox.append(board[(box_MIndex-a)][b]) #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list

               if tempPossibleBox not in possibleBoxOrder: #we only want to add possible Box order if it is different than the rest of already saved possible orders
                  possibleBoxOrder.append(tempPossibleBox) #add temp list to end of big list

                  pBoxOrderCount += 1 
                  #after adding the UNIQUE completed Box order to the list, we need to increment this so next time a possible order is found in the next call to this function, it can be added properly
                  print(f" Unique solution found...tempPossibleBox: {tempPossibleBox}\n PossibleBoxOrder: {possibleBoxOrder}\n pOrderCount: {pBoxOrderCount}")

               elif tempPossibleBox in possibleBoxOrder:

                  print("\n Oh! It looks like that possible order has already been saved to the list, so we aren't saving it, moving on... ")
                  print(f" PossibleBoxOrder: {possibleBoxOrder}\n pOrderCount: {pBoxOrderCount}")

               board = copy.deepcopy(board_backup) #re write regular board back to starting point to try different order of numbers again
         
               #we should increment deadEndCount in order to check the next possible order of vals, otherwise it infintely checks just the first correct order
               deadEndCount += 1

               if (deadEndCount != len(startingVals) ):
                  print(f"\n Checking next possible combination by sending updated deadEndCount({deadEndCount}) to SolveBox recursively...")
                  #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
                  allOrders = sudokuSolveBox(board, bigBoxIndex, startingVals, deadEndCount, possibleBoxOrder, pBoxOrderCount, skippedVals ) 

                  print("\n After saving possible Box order",pBoxOrderCount,", we have checked the rest of the startingvals and finished with", len(allOrders), "possible orders...")

                  return allOrders #need to return the list of possible Boxes after 

               elif (deadEndCount == len(startingVals) ):

                  print("\n So the Box has finished checking every possible combination, it found", pBoxOrderCount, "possible Box order(s)...")

                  print(f"\n PossibleBoxOrder: {possibleBoxOrder}")

                  if (pBoxOrderCount > 1):

                     print(f"\n So Box {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                     skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                     temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different order of numbers again
                     board = copy.deepcopy(board_backup)

                     findEasiestStart.findEasiestStart(board, skippedVals)

                  elif (pBoxOrderCount == 1):

                     #if Box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                     #re save only solution to board before sending the board with the completed box to next start
                     
                     counterD = 1 #set up seperate variable from a to access all 9 vals in possibleOrder while using a to index the overall board properly 
                     #cD =1 results in possibleOrder[0][3- (3)] = [0][0], then [0][4 - (3)]= [0][1], then [0][2], then cD is 0 results in [0][3- (0)] = [0][3], [0][4], [0][5]
                     #then cD = -1 resulting in [0][3-(-3)] = [0][6], [0][7], [0][8]
                     for a in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                        #this way when MIndex = 2 ((BBindex = 1, and then -1, so 1-1=0) + m which is 2), we get 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 1 = board[0-2][3-5]
                        #or when MIndex = 5 ((BBindex = 4, and then -1, so 4-1=3)+ m which is 2), we get 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 4 = board[3-5][3-5]
                        #or when MIndex = 8 ((BBindex = 7, and then -1, so 7-1=6)+ m which is 2), we get 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 7 = board[6-8][3-5]
                     
                        for b in range(3,6):
                           #n index just needs to be 3,4 and 5

                           #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                           board[(box_MIndex-a)][b] = possibleBoxOrder[0][b-(counterD*3)] 

                           #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list
                        counterD -=1

                     print(f"\n Box completed with only possible combination! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
                     pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                     newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                     findEasiestStart.findEasiestStart(board, newSkippedVals)

            #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleBoxOrder list, 
            elif (board[box_MIndex][box_NIndex] != "." and m == 2 and n == 2 and deadEndCount == len(startingVals) ):

               print(f"\n All possible orders of values for this box have been found...\n Checking if more than 2... There is/are", pBoxOrderCount)

               if (pBoxOrderCount > 1):

                  print(f"\n So Box: {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                  skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                  temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
                  board = copy.deepcopy(board_backup)

                  findEasiestStart.findEasiestStart(board, skippedVals )

               elif (pBoxOrderCount == 1):

                  #if box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                  #re save only solution to board before sending the board with the completed box to next start
                     
                  counterE = 1 #set up seperate variable from c to access all 9 vals in possibleOrder while using c to index the overall board properly 
                  #cE =1 results in possibleOrder[0][3- (3)] = [0][0], then [0][4 - (3)]= [0][1], then [0][2], then cE is 0 results in [0][3- (0)] = [0][3], [0][4], [0][5]
                  #then cE = -1 resulting in [0][3-(-3)] = [0][6], [0][7], [0][8]
                  for c in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                     #this way when MIndex = 2 ((BBindex = 1, and then -1, so 1-1=0) + m which is 2), we get 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 1 = board[0-2][3-5]
                     #or when MIndex = 5 ((BBindex = 4, and then -1, so 4-1=3)+ m which is 2), we get 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 4 = board[3-5][3-5]
                     #or when MIndex = 8 ((BBindex = 7, and then -1, so 7-1=6)+ m which is 2), we get 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 7 = board[6-8][3-5]
                     
                     for d in range(3,6):
                        #n index just needs to be 3,4 and 5

                        #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                        board[(box_MIndex-c)][d] = possibleBoxOrder[0][d-(counterE*3)] 

                        #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list
                     counterE -=1

                  print(f"\n Box completed with only possible combination! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                  newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                  findEasiestStart.findEasiestStart(board, newSkippedVals)


            #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, AND THE DEADENDCOUNT IS MAXXED BEFORE FINISHING ROW
            elif (deadEnd == True and m <= 2 and n <= 2 and deadEndCount == len(startingVals) ):

               print(f"\n All possible orders of values for this box have been tried...\n Checking how many possible... There is/are", pBoxOrderCount)

               if (pBoxOrderCount > 1):

                  print(f"\n So Box: {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                  skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                  temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
                  board = copy.deepcopy(board_backup)

                  findEasiestStart.findEasiestStart(board, skippedVals )

               elif (pBoxOrderCount == 1):

                  #if Box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                  #re save only solution to board before sending the board with the completed box to next start
                  
                  rowIndexStart = bigBoxIndex-1 #need to force rowIndex to start with 0, 3 or 6
                  rowIndexEnd = rowIndexStart+3 #need rowIndex to end at either 2, 5 or 8

                  counterF = 1 #set up seperate variable from e to access all 9 vals in possibleOrder while using e to index the overall board properly 
                  #cF =1 results in possibleOrder[0][3- (3)] = [0][0], then [0][4 - (3)]= [0][1], then [0][2], then cF is 0 results in [0][3- (0)] = [0][3], [0][4], [0][5]
                  #then cF = -1 resulting in [0][3-(-3)] = [0][6], [0][7], [0][8]
                  for e in range(rowIndexStart, rowIndexEnd): #CANT USE MIndex since we dont know what m or n is exactly, but need to add each element of the box to the tempPBox list
                     
                     for f in range(3,6):
                        #n index just needs to be 3,4 and 5

                        #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                        board[(e)][f] = possibleBoxOrder[0][f-(counterF*3)] 

                        #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list
                     counterF -=1

                  print(f"\n Box completed with only possible combination after checking every single combo! Sending board to next starting point...\n Clearing Skipped Vals...\n New Board Being Sent: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                  newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                  findEasiestStart.findEasiestStart(board, newSkippedVals)

               elif (pBoxOrderCount < 1):

                  print(f"\n Sorry, no possible combinations found for Box {bigBoxIndex} after trying all possible permutations and reaching a dead end before the end of said Box,\n while the end of the Box contains a '.' still...\n")
                  return possibleRowOrder

         #========================================== END BOX 1, 4 and 7 solves ==========================================================================================================================


         elif (bigBoxIndex == 2 or bigBoxIndex == 5 or bigBoxIndex == 8):

            box_MIndex = m + (bigBoxIndex - 2) #need coordinates to start at (0,6), (3,6), or (6,6)
            box_NIndex = 6 + n 

            if (board[box_MIndex][box_NIndex] == "."): #find every period in the box sent to be solved

               while (newBoxValWorks == False and deadEnd == False and deadEndCount != len(startingVals) ): 
               #find empty cell, put a number in and see if it works, once one works leave loop and check next cell in board

                  for index, x in enumerate(startingVals[deadEndCount]):

                     temp_box_board[box_MIndex][box_NIndex] = str(x) #assign empty space to a number 1-9 and then check validity to see if worth keeping

                     tBoxBoardIsValid = validityChecker.validityChecker(temp_box_board) #pass temp board once so that it doesnt run every if statement below

                     print(f"\n Box 2, 5, or 8, m = {m}, n= {n}, index = {index}, (len(startingVals[deadEndCount])-1) = {(len(startingVals[deadEndCount])-1)}, isValid = {tBoxBoardIsValid}")

                     if (tBoxBoardIsValid == True):
                        #if new val works, then change actual value in the board and check next cell, should stop every cell being forced to be 9
                        board[box_MIndex][box_NIndex] = str(x) #actually change board and then trigger while loop to end
                        #pprint.pprint(temp_board)
                        pprint.pprint(board)
                        newBoxValWorks = True
                        break #exit for loop to force while loop to realize that newValWorks has changed, which will then end up moving forward to the next "." to fill and then check, and so on

                     elif (tBoxBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and m <= 2 and n <=2):

                        deadEnd = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, dead end reached at box {bigBoxIndex}, row {box_MIndex}, col {box_NIndex}, exiting loop and attempting to try next combo...\n Dead End Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different numbers again
                        board = copy.deepcopy(board_backup)
                        #newStart = startingVals[1:] + startingVals[:1] #need to start next loop at next number in starting vals list to get different combo of 9 letters for the row

                        deadEndCount += 1

                        if (deadEndCount <= (len(startingVals)-1)):  #if we still have other combos to try, increment deadEndCount and move on to next combo
                           print(" Starting Values: ",startingVals[deadEndCount-1], "\n New Starting Values: ", startingVals[deadEndCount], "\n")

                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                           #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
                           possibleBoxOrder = sudokuSolveBox(board, bigBoxIndex, startingVals, deadEndCount, possibleBoxOrder, pBoxOrderCount, skippedVals ) 

                           return possibleBoxOrder #exit function after returning from recursive solveBox call, so that it doesn't try any more values after dead end is reached

                        elif (deadEndCount > (len(startingVals)-1) and pBoxOrderCount == 0): #if we finish trying a combo before we get to the last item in the row, and we are out of combos
                           #if we have tried the last value in the last combo of values, and we have 0 possible solutions, we need to quit since we have run out of possible combinations to try
                           print("\n Sorry! We have tried every possible combination of values on box ", bigBoxIndex, ".\n This means the board is not solvable, or that we made a mistake somewhere...\n")
                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )
                           print("\n Exiting Function...")
                           return possibleBoxOrder #exit function without calling solveBox again, since we have reached a full deadend without any solutions

                        elif (deadEndCount > (len(startingVals)-1) and pBoxOrderCount > 0): #if we finish trying a combo before we get to the last item in the Box, and we are out of combos (m!=2)
                           #AND we have more than one possible solution, we need to properly return said list of solutions
                           print("\n We have now tried every possible combination of values on Box", bigBoxIndex, "\n")
                           print(" DeadEndCount Now Equals = ", deadEndCount, "\n StartingVals Length: ", len(startingVals) )

                           break 
                           #if deadendCount maxed but we have solutions, we need to break from this for loop, which will break while loop, and then on the last check of m and n with full deadEndCount, 
                           #we will pick a combo. NOTE: if deadEndCount max hit before m and n is through entire box and the box ends in an empty cell, the ifs that this will go to won't work, since
                           #they need the last item in the box to be a actual number and not a "."

                     elif (tBoxBoardIsValid == False and index == (len(startingVals[deadEndCount])-1) and m == 2 and n == 2):

                        noSolutionFound = True #if we tried all 9 numbers and board is not coming out right, trigger the dead end and try new numbers?
                        print(f"\n Sorry, no solution found for the box {bigBoxIndex}, exiting program...\n Final Board: \n")
                        pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                        return possibleBoxOrder

                  #pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

               if (deadEndCount == len(startingVals) and pBoxOrderCount == 0): #if no more orders of startingVals to try and no possible orders found

                  noSolutionFound = True #if we tried all possible combinations of the values avaliable, and board is not coming out right, trigger the dead end and try new numbers?
                  print(f"\n Sorry, no solution found for the row {bigRowIndex}, deadEndCount = {deadEndCount}, and startingVals Length = {len(startingVals)}, exiting program...\n Final Board: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.

                  return possibleBoxOrder

            #AFTER WHILE LOOP AND X FOR LOOP ENDS, BUT STILL WITHIN N FOR and then M FOR, need to create list containing the valid order that was found and store it in big list containing all 
            #possible orders for this box, should only run on final lap of for loops since m == 2 and n == 2 , and only when dead end count is not full
            #if end of box and end of possible inputs is reached, and board is valid, then box must be correct, so add it to possible orders, and then if deadEndCount is still less than 
            #startingVals length, it means there is still combos to try, so we need to save the Box's order and then try the other options
            if (board[box_MIndex][box_NIndex] != "." and m == 2 and n == 2 and deadEndCount != len(startingVals) ):
               print(f"\n Possible Box Order Found! Saving order to possibleBoxOrder...\n Box Being Saved: {bigBoxIndex}")

               for a in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                  #this way when MIndex = 2 ((BBindex = 2, and then -2, so 2-2=0) + m which is 2), we get 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 2 = board[0-2][6-8]
                  #or when MIndex = 5 ((BBindex = 5, and then -2, so 5-2=3)+ m which is 2), we get 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 5 = board[3-5][6-8]
                  #or when MIndex = 8 ((BBindex = 8, and then -2, so 8-2=6)+ m which is 2), we get 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 8 = board[6-8][6-8]
                  for b in range(6,9):
                     #n index just needs to be 6,7 and 8

                     tempPossibleBox.append(board[(box_MIndex-a)][b]) #loop through the complete Box and add each val to list tempPossibleBox to be then stored inside possibleBoxOrder list

               if tempPossibleBox not in possibleBoxOrder: #we only want to add possible Box order if it is different than the rest of already saved possible orders
                  possibleBoxOrder.append(tempPossibleBox) #add temp list to end of big list

                  pBoxOrderCount += 1 
                  #after adding the UNIQUE completed Box order to the list, we need to increment this so next time a possible order is found in the next call to this function, it can be added properly
                  print(f" Unique solution found...tempPossibleBox: {tempPossibleBox}\n PossibleBoxOrder: {possibleBoxOrder}\n pOrderCount: {pBoxOrderCount}")

               elif tempPossibleBox in possibleBoxOrder:

                  print("\n Oh! It looks like that possible order has already been saved to the list, so we aren't saving it, moving on... ")
                  print(f" PossibleBoxOrder: {possibleBoxOrder}\n pOrderCount: {pBoxOrderCount}")

               board = copy.deepcopy(board_backup) #re write regular board back to starting point to try different order of numbers again
         
               #we should increment deadEndCount in order to check the next possible order of vals, otherwise it infintely checks just the first correct order
               deadEndCount += 1

               if (deadEndCount != len(startingVals) ):
                  print(f"\n Checking next possible combination by sending updated deadEndCount({deadEndCount}) to SolveBox recursively...")
                  #pass same old startingvals list, since the deadEndCount is the index to tell it which combo of numbers to try from the list
                  allOrders = sudokuSolveBox(board, bigBoxIndex, startingVals, deadEndCount, possibleBoxOrder, pBoxOrderCount, skippedVals )

                  print("\n After saving possible Box order",pBoxOrderCount,", we have checked the rest of the startingvals and finished with", len(allOrders), "possible orders...")

                  return allOrders #need to return the list of possible Boxes after 

               elif (deadEndCount == len(startingVals) ):

                  print("\n So the Box has finished checking every possible combination, it found", pBoxOrderCount, "possible Box order(s)...")

                  print(f"\n PossibleBoxOrder: {possibleBoxOrder}")

                  if (pBoxOrderCount > 1):

                     print(f"\n So Box {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                     skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                     temp_row_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different order of numbers again
                     board = copy.deepcopy(board_backup)

                     findEasiestStart.findEasiestStart(board, skippedVals )

                  elif (pBoxOrderCount == 1):

                     #if Box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                     #re save only solution to board before sending the board with the completed box to next start
                     
                     counterG = 2 #set up seperate variable from a to access all 9 vals in possibleOrder while using a to index the overall board properly 
                     #cG =2 results in possibleOrder[0][6- (6)] = [0][0], then [0][7 - (6)]= [0][1], then [0][2], then cG is 1 results in [0][6- (3)] = [0][3], [0][4], [0][5]
                     #then cG = 0 resulting in [0][6-(0)] = [0][6], [0][7], [0][8]

                     for a in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                        #this way when MIndex = 2 ((BBindex = 2, and then -2, so 2-2=0) + m which is 2), we get 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 2 = board[0-2][6-8]
                        #or when MIndex = 5 ((BBindex = 5, and then -2, so 5-2=3)+ m which is 2), we get 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 5 = board[3-5][6-8]
                        #or when MIndex = 8 ((BBindex = 8, and then -2, so 8-2=6)+ m which is 2), we get 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 8 = board[6-8][6-8]
                        for b in range(6,9):
                           #n index just needs to be 6,7 and 8

                           #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                           board[(box_MIndex-a)][b] = possibleBoxOrder[0][b-(counterG*3)] 

                        counterG -= 1
                           

                     print(f"\n Box completed with only possible combination! Sending board to next starting point...\n New Board Being Sent: \n")
                     pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                     newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                     findEasiestStart.findEasiestStart(board, newSkippedVals)

            #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleBoxOrder list, 
            elif (board[box_MIndex][box_NIndex] != "." and m == 2 and n == 2 and deadEndCount == len(startingVals) ):

               print(f"\n All possible orders of values for this box have been found...\n Checking if more than 2... There are", pBoxOrderCount)

               if (pBoxOrderCount > 1):

                  print(f"\n So Box: {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                  skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                  temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
                  board = copy.deepcopy(board_backup)

                  findEasiestStart.findEasiestStart(board, skippedVals )

               elif (pBoxOrderCount == 1):

                  #if box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                  #re save only solution to board before sending the board with the completed box to next start
                     
                  counterH = 2 #set up seperate variable from c to access all 9 vals in possibleOrder while using c to index the overall board properly 
                  #cH =2 results in possibleOrder[0][6- (6)] = [0][0], then [0][7 - (6)]= [0][1], then [0][2], then cH is 1 results in [0][6- (3)] = [0][3], [0][4], [0][5]
                  #then cH = 0 resulting in [0][6-(0)] = [0][6], [0][7], [0][8]

                  for c in range(2,-1,-1): #need to change MIndex to start at original boxIndex, and then go up by 1 each loop in order to add each element of the box to the tempPBox list
                     #this way when MIndex = 2 ((BBindex = 2, and then -2, so 2-2=0) + m which is 2), we get 2-2 ->0, then 2-1 ->1, and then 2-0 ->2 ===== box 2 = board[0-2][6-8]
                     #or when MIndex = 5 ((BBindex = 5, and then -2, so 5-2=3)+ m which is 2), we get 5-2 ->3, then 5-1 ->4, and then 5-0 ->5 ===== box 5 = board[3-5][6-8]
                     #or when MIndex = 8 ((BBindex = 8, and then -2, so 8-2=6)+ m which is 2), we get 8-2 ->6, then 8-1 ->7, and then 8-0 ->8 ===== box 8 = board[6-8][6-8]
                     for d in range(6,9):
                        #n index just needs to be 6,7 and 8

                        #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                        board[(box_MIndex-a)][d] = possibleBoxOrder[0][d-(counterH*3)] 

                     counterH -= 1

                  print(f"\n Box completed with only possible combination! Sending board to next starting point...\n New Board Being Sent: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                  newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                  findEasiestStart.findEasiestStart(board, newSkippedVals)


            #if we have tried all possible orders of starting vals, then we should have every possible order in the possibleRowOrder list, AND THE DEADENDCOUNT IS MAXXED BEFORE FINISHING ROW
            elif (deadEnd == True and m <= 2 and n <= 2 and deadEndCount == len(startingVals) ):

               print(f"\n All possible orders of values for this box have been tried...\n Checking how many possible... There are", pBoxOrderCount)

               if (pBoxOrderCount > 1):

                  print(f"\n So Box: {bigBoxIndex} has more than 1 possible combination, so we shouldn't fill it, and instead we should go\n and try another row, column, or box...")

                  skippedVals[2].append(bigBoxIndex) #add this Box to list of Boxes for easiestStart func to skip when choosing starting position

                  temp_box_board = copy.deepcopy(board_backup) #re write temp and regular board back to starting point to try different row, col, or box
                  board = copy.deepcopy(board_backup)

                  findEasiestStart.findEasiestStart(board, skippedVals )

               elif (pBoxOrderCount == 1):

                  #if Box only has one valid solution by the end of checking all permutations, then save the solution to the board and send it to find next starting point
                  #re save only solution to board before sending the board with the completed box to next start

                  rowIndexStart = bigBoxIndex #=======================================================================================================================================
                  #rowIndexEnd 
                     
                  counterI = 2 #set up seperate variable from e to access all 9 vals in possibleOrder while using e to index the overall board properly 
                  #cI =2 results in possibleOrder[0][6- (6)] = [0][0], then [0][7 - (6)]= [0][1], then [0][2], then cI is 1 results in [0][6- (3)] = [0][3], [0][4], [0][5]
                  #then cI = 0 resulting in [0][6-(0)] = [0][6], [0][7], [0][8]

                  for e in range(rowIndexStart, rowIndexEnd): #CANT USE MIndex to find index (we don't know what m or n is exactly), need to use bigBoxIndex instead

                     for f in range(6,9):
                        #n index just needs to be 6,7 and 8

                        #need way to access all 9 vals in possibleOrder and stick 3 into board at a time, in the correct order
                        board[(e)][f] = possibleBoxOrder[0][f-(counterI*3)] 

                     counterI -= 1

                  print(f"\n Row completed with only possible combination after checking every single combo! Sending board to next starting point...\n New Board Being Sent: \n")
                  pprint.pprint(board) #for debugging board after sudokuSolve is finished checking every cell.
                  newSkippedVals = copy.deepcopy(sudokuResetSkips.sudokuResetSkips() ) #gets new list containing 3 empty lists

                  findEasiestStart.findEasiestStart(board, newSkippedVals)

               elif (pBoxOrderCount < 1):

                  print(f"\n Sorry, no possible combinations found for Box {bigBoxIndex} after trying all possible permutations and reaching a dead end before the end of said Box,\n while the end of the Box contains a '.' still...\n")
                  return possibleRowOrder

         #========================================== END BOX 1, 4 and 7 solves ==========================================================================================================================

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
   possible_vals = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] #need list of values to try in the empty cells later (to be sent to solver funcs later)
   filledSubBox = [ [], [], [], [], [], [], [], [], [] ] #need new list to store lists of all the values in each sub-box, at least 9 since there is one val in every box
   
   #Gets the list which represents each row of the board as row, i will function as index of rows inside board
   for i, row in enumerate(boardHARDMODE): 
        
      #need to get every value inside of each row as val, j is index of vals inside each row
      for j, val in enumerate(row):  #look through board until first period is found

         if (boardHARDMODE[i][j] != "."): #if val is NOT a period, put it in list to compare lists 

            #SUB-BOX CHECK val and place all real values in a list for each sub-box  ==================================================================================== SUB-BOX
            index = (i // 3) * 3 + (j // 3) #use floor division to get index of which sub-box to put each val in
            filledSubBox[index].append(boardHARDMODE[i][j])

   biggestBox = max(filledSubBox, key=len)
   indexBiggestBox = filledSubBox.index(biggestBox)


   #generate the remaining values that need to be tried, by finding the items in possible vals that aren't in the box's list
   remainingVals = [item for item in possible_vals if item not in filledSubBox[indexBiggestBox]]

   allPossibleVals = list(itertools.permutations(remainingVals)) #generate list of lists where each list is a different combo of the remaingvals to fill the box



   print("\n", sudokuSolveBox(boardHARDMODE, indexBiggestBox, allPossibleVals, 0, [], 0, [], [], [] ) )
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





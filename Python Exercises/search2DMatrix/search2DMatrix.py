""" Search a 2D Matrix Exercise:

   You are given an m x n integer matrix called matrix with the following two properties:

   - Each row is sorted in non-decreasing order.

   - The first integer of each row is greater than the last integer of the previous row.

   Given an integer target, return true if target is in matrix or false otherwise.

   You must write a solution in O(log(m * n)) time complexity.*****************************

   Example 1: See picture in " prompt_images/search2DMatrixExamples "
   Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
   Output: true

   Example 2: See picture in " prompt_images/search2DMatrixExamples "
   Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
   Output: false

"""
# So O(log(m * n)) complexity means we can use at most one log for loop at a time to check the array's elements, i.e. no nested log loops (= O(logm * logn) != O(logm * n)), 
# O(log(m*n)) is equal to O(logM + logN), and this can be simplified to O(log(max(M,N)), which then can be simplified to O(logN)  )
# O(log n) != O(n), a loop needs to not LINEARLY increase its iterator but INSTEAD MULTIPLY or DIVIDE its iterator to be logarithmic...

# Since the matrix is already sorted smallest int to biggest int, and because the first int of each row is bigger than any value before it in the previous rows, we can use that value to narrow our search
# Sort of like a binary search, where the middle val in a sorted array is checked against the target val, and if the val is bigger or smaller than the target, it will then check the middle val between 
# the first middle val and the last val, or between the starting val and the middle val respectively against the target val and repeat the process until it finds the target val, we can use one loop to 
# check the first val of each row against the target, to find a potential row for the target to be, and then use the second loop to check the rest of that row for the val

def findTargetNum(matrix: list[list[int]], target: int) -> bool:

   #start with binary search of array containing the other arrays first to find which array to check

   start = 0 #set starting index to 0 in order to check first array inside matrix first
   end = len(matrix) - 1 #need index of final array inside matrix
   targetArray = None #create var to store index of the array the next loop will need to look at to find the target, start with null val

   #use while loop instead of for in order to be able to control i's iterator
   while start <= end:

      #get middle array index, which is equal to difference between end and start point floor divided by 2
      #this means it won't return a float, and it returns the next SMALLEST int, ex. 7 // 3 = float 2.33, which is rounded down to next smallest val, or 2
      middleIndex = start + (end - start) // 2

      print(f"\n middleIndex: {middleIndex}, start index: {start}, end index: {end}")

      #get first value of middle index array, 
      firstVal = matrix[middleIndex][0]

      print(f"\n firstVal: {firstVal}, target: {target}")
      
      #check if the firstVAL matches target, then return TRUE
      if firstVal == target:

         print(f"\n firstVal is equal to the target, return true")
         return True

      #if the firstVAL is GREATER than target, we need to check if this is the left most array in the matrix, then we can search the remaining left half of the arrays in the matrix if there are any
      elif firstVal > target:

         print(f"\n firstVal is bigger than target, checking if this is the last searchable array in the matrix...")

         if middleIndex == start:

            print("\n This is the last searchable array inside the matrix, so this means that the current firstVal is the smallest value")
            print(" inside the matrix, which further means that because the target is smaller than this val, the target cannot exist")
            print(" inside the matrix. \n\n Returning False...")
               
            return False #breaks out of while loop and entire function to prevent 2nd while loop from running as well

         elif middleIndex > start: 

            print("\n This is NOT the last array in the matrix... Now changing the end index to search remaing arrays...")

            end = middleIndex - 1 #now the next while loop will find the middle array between the first array and the array before the one that this loop checked

            print(f"\n firstVal is bigger than target, now end index: {end}, next while loop...")


      #if the firstVAL is LESS than target number, we need to check the next array's first value as well to ensure that the target isn't in this array, BUT CANT IF CURRENTLY SEARCHING LAST ARRAY in matrix
      #so check if last array, then check next array's first val, and then finally search the remaining right half of the arrays in the matrix in the next while loop
      elif firstVal < target:

         print(f"\n firstVal is smaller than target, checking if this is the last array in the matrix...")

         if middleIndex == end:

            targetArray = middleIndex 
            print(f"\n This is the last searchable array inside the matrix, so if the target exists, it has to be inside the current array,\n so targetArray index: {targetArray}, exiting first while loop...")
            break #will exit out of while loop

         elif middleIndex < end:

            print("\n This is NOT the last array in the matrix... Now checking the next array's first value...")

            nextFirstVal = matrix[(middleIndex+1)][0]

            print(f"\n nextFirstVal: {nextFirstVal}, target: {target}")

            if nextFirstVal == target: #might as well check if the next first val is the target first

               print(f"\n nextFirstVal is equal to the target, return true")
               return True

            elif nextFirstVal > target: #if the next first val is bigger than target, it can only exist inside the firstVal's array, so we will check that array next

               targetArray = middleIndex 
               print(f"\n nextFirstVal is bigger than target, we now know targetArray index is: {targetArray}, exiting first while loop...")
               break #will exit out of while loop


            elif nextFirstVal < target: #if the next first val is smaller than target, then the target is not in the firstVal's array, so we will change the start point for the next while loop

               start = middleIndex + 1 #now the next while loop will find the middle array between the array after this one currently being checked and the final array

               print(f"\n nextFirstVal is smaller than target, now start index is: {start}, next while loop...")

   #END 1ST WHILE LOOP ===============================================================================================================================================================================      
   #Now that we have a specific array to search for the target, we should do ANOTHER binary search for said target
   print(f"\n targetArray is: {matrix[targetArray]}")   

   start2 = 0
   end2 = len(matrix[targetArray]) - 1 #get last index of targetArray

   while start2 <= end2:

      #get middle array index, which is equal to difference between end2 and start2 points, floor divided by 2
      middleIndex2 = start2 + (end2 - start2) // 2

      print(f"\n middleIndex2: {middleIndex2}, start index 2: {start2}, end index 2: {end2}, target: {target}")
      
      #get middle val from targetArray
      middleVal = matrix[targetArray][middleIndex2]


      #check if the middle val matches target, then return TRUE
      if middleVal == target:

         print(f"\n Mid val ({middleVal}) is equal to the target ({target}), meaning the target val is in the matrix, returning true...")
         return True

      #if the middleVal is GREATER than target number, we want to search the remaining left half of the target array 
      elif middleVal > target:

         end2 = middleIndex2 - 1 #now the next while loop will find the middle val between the first val and the val before the one just checked

         print(f"\n middleVal ({middleVal}) is bigger than target, now end2 index: {end2}, next while loop...")


      #if the middleVal is LESS than target number, we need to search the remaining right half of the array
      elif middleVal < target:

         start2 = middleIndex2 + 1 #now the next while loop will find the middle val between the val that just got checked and the final val in the array

         print(f"\n middleVal ({middleVal}) is smaller than target, now start2 index: {start2}, next while loop...")

   #END 2ND WHILE LOOP ===============================================================================================================================================================================
   #if we have reached here, we never found target val inside the target array (middleVal was never equal to target and start2 is now bigger than end2), so we need to return false
   print(f"\n The second while loop was unable to find the target value ({target}), inside of the targetArray ({matrix[targetArray]})...\n The target value is not inside the matrix...")
   print(f"\n Starting Val Index 2 is now {start2}, which is bigger than the Ending Val Index which is now {end2},\n which means we searched through all of the target array...\n Returning False...")
   return False

def main():
   print("=" * 50)
   print(" Search 2D Matrix EXERCISE")
   print("=" * 50)

   #=========================================================== MATRIX 1 ======================================== DEFAULT EXAMPLE
   matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target1 = 3

   print(f"\n Input matrix 1: {matrix1}, target = {target1}") #print matrix1 and target1 to console,
   print("-" * 50)

   print("\n Output 1:") 
   print("-" * 50)
   print(f"\n Final Result: {findTargetNum(matrix1, target1)} ") 
   print("=" * 50)

   #=========================================================== MATRIX 2 ======================================== DEFAULT EXAMPLE
   matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target2 = 13

   print(f"\n Input matrix 2: {matrix2}, target = {target2}") #print matrix2 and target2 to console,
   print("-" * 50)

   print("\n Output 2:") 
   print("-" * 50)
   print(f"\n Final Result: {findTargetNum(matrix2, target2)} ") 
   print("=" * 50)

   #=========================================================== MATRIX 3 ======================================== MODIFIED EXAMPLE 2 to have target in it
   matrix3 = [[1,3,5,7],[10,11,13,16,20,21],[23,30,34,60]]
   target3 = 13

   print(f"\n Input matrix 3: {matrix3}, target = {target3}") #print matrix3 and target3 to console,
   print("-" * 50)

   print("\n Output 3:") 
   print("-" * 50)
   print(f"\n Final Result: {findTargetNum(matrix3, target3)} ") 
   print("=" * 50)

   #=========================================================== MATRIX 4 ======================================== MODIFIED EXAMPLE 2 to have the first val of next loop be the target
   matrix4 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target4 = 23

   print(f"\n Input matrix 4: {matrix4}, target = {target4}") #print matrix4 and target4 to console,
   print("-" * 50)

   print("\n Output 4:") 
   print("-" * 50)
   print(f"\n Final Result: {findTargetNum(matrix4, target4)} ") 
   print("=" * 50)

   #=========================================================== MATRIX 5 ======================================== MODIFIED EXAMPLE 2 so target is bigger than any value inside matrix
   matrix5 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target5 = 100

   print(f"\n Input matrix 5: {matrix5}, target = {target5}") #print matrix5 and target5 to console,
   print("-" * 50)

   print("\n Output 5:") 
   print("-" * 50)
   print(f"\n Final Result: {findTargetNum(matrix5, target5)} ") 
   print("=" * 50)

    #=========================================================== MATRIX 6 ======================================== MODIFIED EXAMPLE 2 so target is smaller than any value inside matrix
   matrix6 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
   target6 = 0

   print(f"\n Input matrix 6: {matrix6}, target = {target6}") #print matrix6 and target6 to console,
   print("-" * 50)

   print("\n Output 6:") 
   print("-" * 50)
   print(f"\n Final Result: {findTargetNum(matrix6, target6)} ") 
   print("=" * 50)

   #======================================================== FINAL REMARKS ======================================
   print("\n Final Remarks:") 
   print("-" * 50)
   print("\n So I ended up doing a Binary search over the first value in each row of the matrix to find which row could contain")
   print("\n the target value, and then I did a 2nd Binary search over the values in said row, to find if the target value exists")
   print("\n within it or not...\n\n\n The first Binary search's complexity takes O(log m) time, where m is the number of rows in the matrix.")
   print("\n So its logarithmic.\n\n\n The second Binary search's complexity takes O(log n) time, where n is the number of columns in the target array.")
   print("\n So its also logarithmic.\n\n\n Therefore since both binary searches are logarithmic algorithms, and I did not nest the 2nd inside the first, ")
   print("\n the overall time complexity is:\n\n\n O(log m + log n), which is equal to the required complexity of O(log(m*n))...")
   print("\n\n See LOG PRODUCT RULE: 'the sum of logarithms is the logarithm of the product -> log m + log n = log(m * n)' \n")
   print("-" * 50)
   print(" Explanation of Examples:")
   print("-" * 50)
   print("\n\n I ran the 2 examples from the example itself first, then altered matrix 2 to contain 13 & 21 inside of its 2nd array")
   print("\n in order to check if the function could find the target 13 properly if the target wasn't an array's first value, and ")
   print("\n if the arrays were different lengths, and it does!")
   print("\n\n Then in matrix 4, I used matrix 2 and a target of 23 to test if the first while loop would find the target after")
   print("\n checking the nextFirstVal while checking the array [10,11,16,20]. It checks 10, sees that it's smaller than 23,")
   print("\n then it checks the next array and finds 23, returning true immediately like intended.")
   print("\n\n Then in matrix 5, I used matrix 2 and a target of 100 to test if the function properly checks for a target that")
   print("\n is bigger than any value in the matrix. Previously, it was creating an indexing issue when the nextFirstVal is")
   print("\n calculated when the last searchable array is currently being checked, since nextFirstVal = matrix[middleIndex + 1],")
   print("\n and if its the last searchable index, middleIndex + 1 doesn't exist. Now it correctly deduces that if the current")
   print("\n middleIndex is the last searchable array inside matrix and the firstVal of that array is smaller than the target,")
   print("\n than the only possible place for the target to exist is the current array, and sends this targetArray to the next")
   print("\n while loop to be searched there...")
   print("\n\n Then in matrix 6, I used matrix 2 and a target of 0 to test if the function properly checks for a target that")
   print("\n is smaller than any value in the matrix. Previously, it was creating an indexing issue when the last searchable")
   print("\n array is currently being checked and the firstVal is bigger than the target, since the first while loop just sets")
   print("\n the end index to be a negative index after this happens, and then exits its loop. Then when the 2nd while loop goes")
   print("\n to run, it can't use targetArray as an index for the matrix, since the first while loop never set it properly.")
   print("\n So now if the first loop finds the firstVal of the last searchable array in the matrix to be bigger than the target,")
   print("\n it immediately returns false (since this means the target cannot exist inside the matrix), and prevents the 2nd while")
   print("\n loop from running and reaching the indexing issue with targetArray. Also, it now prevents setting the end index to a")
   print("\n negative int, since the end index is only reduced if there are still searchable arrays remaing in the matrix.\n")
   print("-" * 50)
   print(" Note:")
   print("-" * 50)
   print("\n Because of how the example is presented, I never created any test cases to check if the function works with a")
   print("\n matrix that is unsorted, sorted diffently than lowest to highest int, or contains anything other than ints etc.,")
   print("\n and the same applies to a target value that isn't an int etc...")


if __name__ == "__main__":
   main()
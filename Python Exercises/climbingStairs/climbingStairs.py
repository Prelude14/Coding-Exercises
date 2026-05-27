""" Climbing Stairs Exercise:

   You are climbing a staircase. It takes n steps to reach the top.

   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

   Example 1: 
   Input: n = 2
   Output: 2
   Explanation: There are two ways to climb to the top.
   1. 1 step + 1 step
   2. 2 steps

   Example 2: 
   Input: n = 3
   Output: 3
   Explanation: There are three ways to climb to the top.
   1. 1 step + 1 step + 1 step
   2. 1 step + 2 steps
   3. 2 steps + 1 step


# So to start, it seems like we just need to take the input "n", then check if it is cleanly divisible by 2 (everything should be divisble by 1 as long as not a negative or a string), and then
# check for all the other different ways to combine 1 and 2 steps to make the number. As n increases, the amount of permutations is going to increase quite fast, need to import "itertools"


"""
import pprint #want this to print out the step lists in more readable format
import itertools #need .permutations() in order to get each solver function to try every possible combo of numbers
import copy #need a way to create an entirely new copy of a list, this is probably overkill for just a regular list of ints, but I like how this tool works

"""
def calcSteps(top: int) -> int:
   allStepPermutations = [] #empty list that will contain each list of possible combos of 1 and 2 steps to equal n

   if (top >  0):
      #======================================================================================================================================== OneStep 
      print("\n Input received is VALID (an INT that is NOT Negative or equal to 0)...now calculating routes to top...")

      total = 1 # start total at 1 since we know if the number is greater than 0 that we can always get there one step at a time (every number > 0 is cleanly divisble by 1)

      oneStepEach = [] #create and fill list to show order of steps to reach n using 1 step at a time
      for i in range(0, top):
         oneStepEach.append(1)

      print(f"\n total = {total}, and oneStepEach = \n")
      pprint.pprint(oneStepEach)

      print("\n Adding oneStepEach to allStepPermutations...\n allStepPermutations = \n")
      allStepPermutations.append(oneStepEach)
      pprint.pprint(allStepPermutations)

      #======================================================================================================================================== TwoSteps
      #now check if n is cleanly divisble by 2 to see if we can also get there using 2 steps at a time cleanly (no left over step)
      doubleStepCheck = top % 2 
      print("\nChecking n%2...")

      if (doubleStepCheck == 0): 

         #this means n has no left overs after being divided by 2 ============================================== CAN USE 2 STEPS ALL THE WAY
         total += 1 
         print(f"\n VALID!\n doubleStepCheck = {doubleStepCheck}, top / 2 = {top/2},\n total now equals: {total} ")

         twoStepsEach = [] #create and fill list to show order of steps to reach n using 2 steps at a time
         for j in range(0, (int(top/2))):
            twoStepsEach.append(2)

         print(f"\n twoStepsEach: \n")
         pprint.pprint(twoStepsEach)

         print("\n Adding twoStepsEach to allStepPermutations...\n allStepPermutations = \n")
         allStepPermutations.append(twoStepsEach)
         pprint.pprint(allStepPermutations)

      elif (doubleStepCheck == 1):

         #this means n has 1 left over after being divided by 2    =============================================== CANNOT USE 2 STEPS ALL THE WAY
         print(f"\n INVALID!\n doubleStepCheck = {doubleStepCheck}, top / 2 = {top/2},\n total still equals: {total} ")

         #now we need to tweak top to figure out new combination using a mix of both steps
         print("\nChecking top-1...")

         mixSteps = [] #create and fill list to show order of steps to reach n using both kinds of steps at a time
         for x in range(0, (int((top-1)/2))):
            mixSteps.append(2)

         mixSteps.append(1)

         print(f"\n mixSteps: \n")
         pprint.pprint(mixSteps)

         print("\n Adding mixSteps to allStepPermutations...\n allStepPermutations = \n")
         allStepPermutations.append(mixSteps)
         pprint.pprint(allStepPermutations)


      #now check possible permutations of 1 and 2 to equal n

   else:

      print("\n ERROR: Input received is INVALID (an INT that IS Negative or equal to 0)...please try new input...closing...")
"""


def calcSteps(top: int) -> int:
   allStepPermutations = [] #empty list that will contain each list of possible combos of 1 and 2 steps to equal n

   if (top >  0):
      #======================================================================================================================================== OneStep 
      print("\n Input received is VALID (an INT that is NOT Negative or equal to 0)...now calculating routes to top...")

      total = 1 # start total at 1 since we know if the number is greater than 0 that we can always get there one step at a time (every number > 0 is cleanly divisble by 1)

      oneStepEach = [] #create and fill list to show order of steps to reach n using 1 step at a time
      for i in range(0, top):
         oneStepEach.append(1)

      print(f"\n total = {total}, and oneStepEach = \n")
      pprint.pprint(oneStepEach)

      print("\n Adding oneStepEach to allStepPermutations...\n allStepPermutations = \n")
      allStepPermutations.append(oneStepEach)
      pprint.pprint(allStepPermutations)

      #======================================================================================================================================== Check OneStep
      # check if the length of OneStepEach is even or odd, if odd, we know we can't use only two steps to get there, we will need to replace some ones with twos to get rest of combos
      doubleStepCheck = len(oneStepEach) % 2 
      print("\n Checking length of oneStepEach %2...")

      

      #this means n has 1 left over after being divided by 2    =============================================== CANNOT USE 2 STEPS ALL THE WAY
      print(f"\n INVALID!\n doubleStepCheck = {doubleStepCheck}, top / 2 = {top/2},\n total still equals: {total} ")

      #now we need to tweak top to figure out new combination using a mix of both steps
      print("\n Checking top-1...")

      j = int( (top-1) /2)

      print(f"\n (top-1) /2 = {j}")

      tempLastSteps = copy.deepcopy(oneStepEach) #define lastSteps list as oneStepEach first, then this will change on every iteration of loop in order to replace all 1s with 2s that are possible
      print(f"\n tempLastSteps = \n")
      pprint.pprint(tempLastSteps)

      for x in range(0, j): # need a new list for every 2 steps that can fit into n

         mixSteps = [] # create and fill list to show order of steps to reach n using both kinds of steps at a time, RESETS EACH MAIN LOOP

         for m in range(0,x+1): 
            mixSteps.append(2) #fill beginning of list with as many 2s as the x that the loop is currently on

         """
         #read oneStepEach list starting at x * 2 as the index to find what pair of 1s to replace with a 2
         tempStepIndex = x*2
         print(f"\n tempStepIndex = {tempStepIndex}")
         """

         newLength = len(tempLastSteps)-2 #need to put entire last list into this new list. except replace two 1s with a 2 upon each iteration, so this needs to be 2 less than last list each time
         #NOT 1 LESS BECAUSE we add the 2 first and then need to run through the last list's remaining 1s, which the 2 replaces 2 1s in the list, 

         for y in range(0, newLength): # run through as much items as the last list had minus one item

            #if (tempLastSteps[y] == 1): #if beginning of x loop, the first index should be a 1, 
            mixSteps.append(1) #add the rest of the ones from the last list

         print(f"\n mixSteps: \n")
         pprint.pprint(mixSteps)

         print("\n Adding mixSteps to allStepPermutations...\n allStepPermutations = \n")
         allStepPermutations.append(mixSteps)
         pprint.pprint(allStepPermutations)

         tempLastSteps = copy.deepcopy(mixSteps) #change last steps list to now be the list with the new 2 in it, so next loop doesn't add extra 1 each time

               




      
   else:

      print("\n ERROR: Input received is INVALID (an INT that IS Negative or equal to 0)...please try new input...closing...")


def main():
   print("=" * 50)
   print(" Climbing Stairs EXERCISE")
   print("=" * 50)

   #=========================================================== N = 2 ======================================== DEFAULT EXAMPLE 1
   target1 = 3

   print(f"\n Input 1: n = {target1}") #print first n to console
   print("-" * 50)

   print("\n Output 1:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target1)} ") 
   print("=" * 50)

   """
   #=========================================================== N = 3 ======================================== DEFAULT EXAMPLE 2
   target2 = 3

   print(f"\n Input 2: n = {target2}") #print n to console
   print("-" * 50)

   print("\n Output 2:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target2)} ") 
   print("=" * 50)

   """
   """
   #=========================================================== N = 0 ======================================== CUSTOM EXAMPLE 1
   target3 = 0

   print(f"\n Input 3: n = {target3}") #print n to console
   print("-" * 50)

   print("\n Output 3:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target3)} ") 
   print("=" * 50)

   #=========================================================== N = -1 ======================================== CUSTOM EXAMPLE 2
   target4 = -1

   print(f"\n Input 4: n = {target4}") #print n to console
   print("-" * 50)

   print("\n Output 4:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target4)} ") 
   print("=" * 50)

   """
   """
   #=========================================================== N = "string" ======================================== CUSTOM EXAMPLE 3
   target5 = "string"

   print(f"\n Input 5: n = {target5}") #print n to console
   print("-" * 50)

   print("\n Output 5:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target5)} ") 
   print("=" * 50)
   """
   
   """
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
   """


if __name__ == "__main__":
   main()
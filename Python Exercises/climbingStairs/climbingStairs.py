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
def calcSteps1(top: int) -> int:
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
#=================================== END calcSteps1 ====================================================================================================================

"""
def calcSteps2(top: int) -> int:
   allStep1Permutations = [] #empty list that will contain each list of possible combos of 1 and 2 steps to equal n

   if (top >  0):
      #======================================================================================================================================== OneStep 
      print("\n Input received is VALID (an INT that is NOT Negative or equal to 0)...now calculating routes to top...")

      total = 1 # start total at 1 since we know if the number is greater than 0 that we can always get there one step at a time (every number > 0 is cleanly divisble by 1)

      oneStepEach = [] #create and fill list to show order of steps to reach n using 1 step at a time
      for i in range(0, top):
         oneStepEach.append(1)

      print(f"\n total = {total}, and oneStepEach = \n")
      pprint.pprint(oneStepEach)

      print("\n Adding oneStepEach to allStep1Permutations...\n allStep1Permutations = \n")
      allStep1Permutations.append(oneStepEach)
      pprint.pprint(allStep1Permutations)

      #======================================================================================================================================== Check OneStep
      
      
      # check if the length of OneStepEach is even or odd, if odd, we know we can't use only two steps to get there, we will need to replace some ones with twos to get rest of combos
      #doubleStepCheck = len(oneStepEach) % 2 
      #print("\n Checking length of oneStepEach %2...")

      #this means n has 1 left over after being divided by 2    =============================================== CANNOT USE 2 STEPS ALL THE WAY
      #print(f"\n INVALID!\n doubleStepCheck = {doubleStepCheck}, top / 2 = {top/2},\n total still equals: {total} ")


      #now we need to tweak top to figure out new combination using a mix of both steps
      print("\n Figuring out how many 2s can be used to replace pairs of 1 and still reach n...")

      j = int( top /2) #int gets rids of float value of decimial and rounds down if n is an uneven number

      print(f"\n int(top / 2) = j = {j}")

      tempLastSteps = copy.deepcopy(oneStepEach) #define lastSteps list as oneStepEach first, then this will change on every iteration of loop in order to replace all 1s with 2s that are possible
      print(f"\n tempLastSteps = \n")
      pprint.pprint(tempLastSteps)

      for x in range(0, j): # need a new list for every 2 steps that can fit into n

         #debug what order was used on each loop
         #print(f"\n tempLastSteps = \n")
         #pprint.pprint(tempLastSteps)


         mixSteps = [] # create and fill list to show order of steps to reach n using both kinds of steps at a time, RESETS EACH MAIN LOOP

         for m in range(0,x+1): 
            mixSteps.append(2) #fill beginning of list with as many 2s as the x that the loop is currently on

         #read oneStepEach list starting at x * 2 as the index to find what pair of 1s to replace with a 2
         #tempStepIndex = x*2
         #print(f"\n tempStepIndex = {tempStepIndex}")


         newLength = len(tempLastSteps)-2 #need to put entire last list into this new list. except replace two 1s with a 2 upon each iteration, so this needs to be 2 less than last list each time
         #NOT 1 LESS BECAUSE we add the 2 above first, and then need to run through the last list's remaining 1s, which the 2 replaces 2 1s in the list, 

         if (newLength > 1): #if there is at least 2 more items in the last list, we want to add them to this new list (DONT ADD ANY IF ONLY ONE 1 REMAINS, WILL BREAK MATH TO REACH N)
            print(f"\n newLength = {newLength}, adding rest of 1s to new list")
            for y in range(0, newLength): # run through as much items as the last list had minus one item

               #if (tempLastSteps[y] == 1): #if beginning of x loop, the first index should be a 1, 
               mixSteps.append(1) #add the rest of the ones from the last list

         mixStepsTotal = sum(mixSteps)

         print(f"\n mixStepsTotal before check: {mixStepsTotal}, and mixSteps before check: \n")
         pprint.pprint(mixSteps)


         if (mixStepsTotal == top):

            print("\n MixSteps adds up to n correctly!")
            proofString = "+".join(str(items) for items in mixSteps)
            print(f"\n n = {top}, and {top} = {proofString}")

            print("\n Finding other permutations of current MixSteps...")
            mixStepsPermutations = set(itertools.permutations(mixSteps)) # SET of possible combos in order to get rid of repeating combos

            print("\n mixStepsPermutations = \n")
            pprint.pprint(mixStepsPermutations)

            if (len(mixStepsPermutations) > 1): #if there are other possible orders of mixSteps, save each list into main list

               print("\n MORE THAN 1 POSSIBLE ORDER!")
               #pprint.pprint(mixStepsPermutations)

               print("\n Adding all of mixStepsPermutations to allStep1Permutations...\n allStep1Permutations = \n")

               for order in mixStepsPermutations:

                  allStep1Permutations.append(order)

               pprint.pprint(allStep1Permutations)

            elif (len(mixStepsPermutations) == 1): #if there are no other possible orders of mixSteps, just save the one version to the big list

               print("\n ONLY 1 POSSIBLE ORDER!")
               #pprint.pprint(mixStepsPermutations)

               print("\n Adding mixStepsPermutations to allStep1Permutations...\n allStep1Permutations = \n")
               allStep1Permutations.append(mixStepsPermutations)
               pprint.pprint(allStep1Permutations)

            tempLastSteps = copy.deepcopy(mixSteps) #change last steps list to now be the list with the new 2 in it, so next loop doesn't add extra 1 each time

         elif (mixStepsTotal < top):

            print("\n MixSteps is LESS THAN N!\n Not adding mixSteps to allStepPermutations...")

            print(f"\n Adding last of 1s to new list...")
           
            mixSteps.append(1) #add the rest of the ones from the last list

            mixStepsTotal2 = sum(mixSteps)

            print(f"\n mixStepsTotal2 before 2nd check: {mixStepsTotal2}, and mixSteps before 2nd check: \n")
            pprint.pprint(mixSteps)

            if (mixStepsTotal2 == top):

               print("\n MixSteps adds up to n correctly!")
               proofString2 = "+".join(str(values) for values in mixSteps)
               print(f"\n n = {top}, and {top} = {proofString2}")

               print("\n Finding other permutations of current MixSteps...")
               mixStepsPermutations2 = set(itertools.permutations(mixSteps)) # SET of possible combos in order to get rid of repeating combos

               print("\n mixStepsPermutations2 = \n")
               pprint.pprint(mixStepsPermutations2)

               if (len(mixStepsPermutations2) > 1): #if there are other possible orders of mixSteps, save each list into main list

                  print("\n MORE THAN 1 POSSIBLE ORDER!")
                  #pprint.pprint(mixStepsPermutations2)

                  print("\n Adding all of mixStepsPermutations2 to allStep1Permutations...\n allStep1Permutations = \n")

                  for orders in mixStepsPermutations2:

                     allStep1Permutations.append(orders)

                  pprint.pprint(allStep1Permutations)

               elif (len(mixStepsPermutations2) == 1): #if there are no other possible orders of mixSteps, just save the one version to the big list

                  print("\n ONLY 1 POSSIBLE ORDER!")
                  #pprint.pprint(mixStepsPermutations2)

                  print("\n Adding mixStepsPermutations2 to allStep1Permutations...\n allStep1Permutations = \n")
                  allStep1Permutations.append(mixStepsPermutations2)
                  pprint.pprint(allStep1Permutations)

               tempLastSteps = copy.deepcopy(mixSteps) #change last steps list to now be the list with the new 2 in it, so next loop doesn't add extra 1 each time

         elif (mixStepsTotal > top):

            print("\n MixSteps is MORE THAN N!\n Not adding mixSteps to allStepPermutations...")

            print(f"\n Subtracting last item from new list (should be a 1)...")
           
            del mixSteps[-1] #delete the last of the ones from the last list

            mixStepsTotal2 = sum(mixSteps)

            print(f"\n mixStepsTotal2 before 2nd check: {mixStepsTotal2}, and mixSteps before 2nd check: \n")
            pprint.pprint(mixSteps)

            if (mixStepsTotal2 == top):

               print("\n MixSteps adds up to n correctly!")
               proofString2 = "+".join(str(values) for values in mixSteps)
               print(f"\n n = {top}, and {top} = {proofString2}")

               print("\n Finding other permutations of current MixSteps...")
               mixStepsPermutations2 = set(itertools.permutations(mixSteps)) # SET of possible combos in order to get rid of repeating combos

               print("\n mixStepsPermutations2 = \n")
               pprint.pprint(mixStepsPermutations2)

               if (len(mixStepsPermutations2) > 1): #if there are other possible orders of mixSteps, save each list into main list

                  print("\n MORE THAN 1 POSSIBLE ORDER!")
                  #pprint.pprint(mixStepsPermutations2)

                  print("\n Adding all of mixStepsPermutations2 to allStep1Permutations...\n allStep1Permutations = \n")

                  for orders in mixStepsPermutations2:

                     allStep1Permutations.append(orders)

                  pprint.pprint(allStep1Permutations)

               elif (len(mixStepsPermutations2) == 1): #if there are no other possible orders of mixSteps, just save the one version to the big list

                  print("\n ONLY 1 POSSIBLE ORDER!")
                  #pprint.pprint(mixStepsPermutations2)

                  print("\n Adding mixStepsPermutations2 to allStep1Permutations...\n allStep1Permutations = \n")
                  allStep1Permutations.append(mixStepsPermutations2)
                  pprint.pprint(allStep1Permutations)

               tempLastSteps = copy.deepcopy(mixSteps) #change last steps list to now be the list with the new 2 in it, so next loop doesn't add extra 1 each time




      #============================================ END OF X FOR LOOP (should have all step 1 permutations ready) ======================================================

      #now we have the list of 1 steps only, the list with 2 steps only if applicable, and each possible version of a list containing a combo of 2 and 1s to reach n,

      #NEED TO FIND HOW MANY ITEMS IN BIG LIST AND RETURN IT
      return len(allStep1Permutations)
      
   else:

      print("\n ERROR: Input received is INVALID (an INT that IS Negative or equal to 0)...please try new input...closing...")
""" #=================================== END calcSteps2 ====================================================================================================================


def calcSteps(top: int) -> int:

   fullStepsList = [] #empty list to store all possible permutations of steps to reach n

   oneSteps = []

   if (top > 0): #CHECK THAT N IS VALID POSTIVE NUMBER ABOVE 0 ====================================

      for i in range(0, top):

         oneSteps.append(1)

      print(f" Top = {top}, OneSteps = \n")
      pprint.pprint(oneSteps)

      print("\n Adding oneSteps to fullStepsList...\n fullStepsList = \n")
      fullStepsList.append(oneSteps)
      pprint.pprint(fullStepsList)

      #now we need to figure out new combinations using a mix of both steps
      #NEED to now begin replacing pairs of 1s with a single 2 using the original list of 1s, until there is no more pairs left to replace and need to ensure the total of each list remains equal to n
      print("\n Figuring out how many 2s can be used to replace pairs of 1 and still reach n...")
      #print("\n If n%2 == 0, the final possible list's length will be equal to n/2, and will be all 2s...")
      #print("\n If n%2 != 0, the final possible list's length will be equal to (n/2)+1, and will be ONE 1 and REST 2s...")

      tempLastSteps = copy.deepcopy(oneSteps) #define lastSteps list as oneSteps first, then this will change on every iteration of loop in order to replace all 1s with 2s that are possible
      print(f"\n tempLastSteps = \n")
      pprint.pprint(tempLastSteps)

      #check if n is even or odd using %2, using the oneSteps list
      nEvenOrOdd = len(oneSteps) % 2 
      print(f"\n Checking length of oneSteps %2... It equals: {nEvenOrOdd}, top/2 = {(top/2)}")

      if (nEvenOrOdd == 0):   #==================================================================================================================== EVEN N 

         print(f"\n Length is EVEN, so n is also even, this means the last combination of steps will be all 2s...")

         howMany2sEVEN = int(top / 2)

         for x in range(0, howMany2sEVEN): # need a new list for every 2 steps that can replace a pair of 1s and still add up to n

            #debug what order was used on each loop
            """
            print(f"\n tempLastSteps = \n")
            pprint.pprint(tempLastSteps)
            """
            #check that there is at least 1 pair of 1s left in the current list
            count1s = 0
            index1st1 = 0
            for index, steps in enumerate(tempLastSteps):

               if (steps == 1 and count1s == 0): #if FIRST 1, get index of that item

                  index1st1 = index
                  count1s += 1
                  print(f"\n First 1 found at index: {index1st1}, count1s now: {count1s}")

               elif (steps == 1 and count1s == 1): #if SECOND 1, confirm there is at least 2 1s left and break loop

                  count1s += 1
                  print(f"\n Second 1 found at index: {index}, count1s now: {count1s}, breaking from pair checking Loop...")
                  break

               #elif (steps == 2 and count1s == 0 and index == len(tempLastSteps)): #this means there are no more 1s left in the list to replace, shouldn't happen***********

            #change last steps list to now be the list with the new 2 in it, so next loop doesn't add extra 1 each time
            tempLastSteps = copy.deepcopy(put2InList(tempLastSteps, index1st1))

            print(f"\n tempLastSteps after being sent to put2InList = ")
            pprint.pprint(tempLastSteps)

            print("\n Checking if new list is still equal to original n...\n Sending List to validateSumAndFindPermutations...")
            mixStepsPermutations = copy.deepcopy(validateSumAndFindPermutations(tempLastSteps, top))

            print("\n Received mixStepPermutations from validateSumAndFindPermutations...\n Sending to savePermutations to be saved...")
            fullStepsList = copy.deepcopy(savePermutations(mixStepsPermutations, fullStepsList))

            print("\n Received fullStepsList from savePermutations...\n fullStepsList = \n")
            pprint.pprint(fullStepsList)


      elif (nEvenOrOdd != 0):   #==================================================================================================================== ODD N  

         print(f"\n Length is ODD, so n is also odd, this means the last combination of steps will end in a 1 and the rest are 2s...")

         howMany2sODD = int( (top-1) / 2)

         for y in range(0, howMany2sODD): # need a new list for every 2 steps that can replace a pair of 1s and still add up to n

            #debug what order was used on each loop
            """
            print(f"\n tempLastSteps = \n")
            pprint.pprint(tempLastSteps)
            """
            #check that there is at least 1 pair of 1s left in the current list
            count1sODD = 0
            index1st1ODD = 0
            for indexODD, stepsODD in enumerate(tempLastSteps):

               if (stepsODD == 1 and count1sODD == 0): #if FIRST 1, get index of that item

                  index1st1ODD = indexODD
                  count1sODD += 1
                  print(f"\n First 1 found at index: {index1st1ODD}, count1s now: {count1sODD}")

               elif (stepsODD == 1 and count1sODD == 1): #if SECOND 1, confirm there is at least 2 1s left and break loop

                  count1sODD += 1
                  print(f"\n Second 1 found at index: {indexODD}, count1s now: {count1sODD}, breaking from pair checking Loop...")
                  break

               #elif (steps == 2 and count1s == 0 and index == len(tempLastSteps)): #this means there are no more 1s left in the list to replace, shouldn't happen***********

            #change last steps list to now be the list with the new 2 in it, so next loop doesn't add extra 1 each time
            tempLastSteps = copy.deepcopy(put2InList(tempLastSteps, index1st1ODD))

            print(f"\n tempLastSteps after being sent to put2InList = ")
            pprint.pprint(tempLastSteps)

            print("\n Checking if new list is still equal to original n...\n Sending List to validateSumAndFindPermutations...")
            mixStepsPermutations = copy.deepcopy(validateSumAndFindPermutations(tempLastSteps, top))

            print("\n Received mixStepPermutations from validateSumAndFindPermutations...\n Sending to savePermutations to be saved...")
            fullStepsList = copy.deepcopy(savePermutations(mixStepsPermutations, fullStepsList))

            print("\n Received fullStepsList from savePermutations...\n fullStepsList = \n")
            pprint.pprint(fullStepsList)


         #===================== END Y FOR =====================

      #NEED TO FIND HOW MANY ITEMS IN BIG LIST AFTER ALL LOOPS ARE DONE AND RETURN IT
      return len(fullStepsList)

   else: #IF N IS LESS THAN OR EQUAL TO 0, its INVALID

      print("\n ERROR: Input received is INVALID (an INT that IS Negative or equal to 0)...please try new input...closing...")





#function to make new version of tempList that replaces the first 1 with a 2 and deletes the 2nd 1 in the list,
def put2InList(tempList: list[int], index1st1: int) -> list[int]:

   newList = []

   for index, steps in enumerate(tempList):

         if (steps == 2):
            #print(f"\n put2InList found 2s in list, putting them in new list...")
            newList.append(2)

         elif (steps == 1 and index == index1st1):

            #print(f"\n put2InList found the FIRST 1 in the list, replacing it with a 2...")
            newList.append(2) #still add a 2, but this time its in place of the first 1 in the original list

         elif (steps == 1 and index == (index1st1+1) ):

            print(f"\n put2InList found the second 1 in the list, and it is skipping it...")

         elif (steps == 1 and index > (index1st1+1) ):

            #print(f"\n put2InList found the rest of the 1s in the rest of the list, putting them in new list...")
            newList.append(1)

   print(f"\n put2InList created a new list by replacing one pair of 1s with a 2...\n newList =")
   pprint.pprint(newList)

   return newList


#function that checks if a list adds up to n and then finds all permutations if it does
def validateSumAndFindPermutations(tempList: list[int], top: int) -> list[int]:

   tempSum = sum(tempList)

   if (tempSum == top):

      print("\n tempList adds up to n correctly!")
      proofString = "+".join(str(values) for values in tempList)
      print(f" n = {top}, and {top} = {proofString}")

      if (len(tempList) > 1): #if received a list with more than 1 item, than there should be permutations to find

         print("\n Finding other permutations of current tempList...")
         mixStepsPermutations = set(itertools.permutations(tempList)) # SET of possible combos in order to get rid of repeating combos

         print(" mixStepsPermutations = \n")
         pprint.pprint(mixStepsPermutations)

         print("\n Sending all permutations back to to calcSteps...")
         return list(mixStepsPermutations) #always send list version of set

      elif (len(tempList) == 1): #if received a list with only 1 item, there is no ther possible order, so no point in finding permutations, just send back same list

         print("\n tempList contains ONLY 1 item, no other possible permutations...")
         print("\n Sending original order back to to calcSteps...")
         return tempList 

      else:
         print("\n Error, len(tempList) < 1, must be an error with a list somewhere...")


   elif (tempSum == (top-1)): #if sent list of ODD LENGTH it will be missing the last 1 it needs to equal n

      print("\n tempList is 1 LESS THAN n! Adding last 1 to list...")
      tempList.append(1)

      tempSum2 = sum(tempList) #check sum again

      if (tempSum2 == top):

         print("\n tempList now adds up to n correctly!")
         proofStringODD = "+".join(str(valuesODD) for valuesODD in tempList)
         print(f" n = {top}, and {top} = {proofStringODD}")

         print("\n Finding other permutations of current tempList...")
         mixStepsPermutations = set(itertools.permutations(tempList)) # SET of possible combos in order to get rid of repeating combos

         print(" mixStepsPermutations = \n")
         pprint.pprint(mixStepsPermutations)

         return list(mixStepsPermutations) #always send list version of set

      elif (tempSum2 != top):
         print("\n Error, tempSum2 != top even after adding a 1 to tempList, must be an error with a list somewhere...")

   else:
      print("\nError, tempSum != top AND tempSum != (top-1), must be an error with a list somewhere...")

#function to save all the permutations of a list to the big main list,
def savePermutations(mixStepsPermutationsList: list[int], tempFullStepsList: list[int]) -> list[int]:

   if (len(mixStepsPermutationsList) > 1): #if there are other possible orders of mixSteps, save each list into main list

      print("\n MORE THAN 1 POSSIBLE ORDER!")
      #pprint.pprint(mixStepsPermutationsList)

      print("\n Adding all of mixStepsPermutationsList to tempFullStepsList...")
      #print("\n Adding all of mixStepsPermutationsList to tempFullStepsList...\n tempFullStepsList = \n")

      for order in mixStepsPermutationsList:

         tempFullStepsList.append(order)

      #pprint.pprint(tempFullStepsList)

   elif (len(mixStepsPermutationsList) == 1): #if there are no other possible orders of mixSteps, just save the one version to the big list

      print("\n ONLY 1 POSSIBLE ORDER!")
      #pprint.pprint(mixStepsPermutationsList)

      print("\n Adding all of mixStepsPermutationsList to tempFullStepsList...")
      #print("\n Adding all of mixStepsPermutationsList to tempFullStepsList...\n tempFullStepsList = \n")
      tempFullStepsList.append(mixStepsPermutationsList)
      #pprint.pprint(tempFullStepsList)

   elif (len(mixStepsPermutationsList) < 1):

      print("\n Error! len(mixStepsPermutations) < 1, must be an error with a list somewhere...")

   return tempFullStepsList

def main():
   print("=" * 50)
   print(" Climbing Stairs EXERCISE")
   print("=" * 50)

   #=========================================================== N = 2 ======================================== DEFAULT EXAMPLE 1
   target1 = 2

   print(f"\n Input 1: n = {target1}") #print first n to console
   print("-" * 50)

   print("\n Output 1:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target1)} ") 
   print("=" * 50)

   
   #=========================================================== N = 3 ======================================== DEFAULT EXAMPLE 2
   target2 = 3

   print(f"\n Input 2: n = {target2}") #print n to console
   print("-" * 50)

   print("\n Output 2:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target2)} ") 
   print("=" * 50)

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
   #=========================================================== N = "string" ======================================== CUSTOM EXAMPLE 3
   target5 = "string"

   print(f"\n Input 5: n = {target5}") #print n to console
   print("-" * 50)

   print("\n Output 5:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target5)} ") 
   print("=" * 50)
   
   """
   
   #=========================================================== N = 12 ======================================== CUSTOM EXAMPLE 4
   target6 = 12

   print(f"\n Input 6: n = {target6}") #print n to console
   print("-" * 50)

   print("\n Output 6:") 
   print("-" * 50)
   print(f"\n Final Result: {calcSteps(target6)} ") 
   print("=" * 50)
   

   
   #======================================================== FINAL REMARKS ======================================
   print("\n Final Remarks:") 
   print("-" * 50)
   print("\n So I ended up writing 3 different versions of this. \n The first ('calcSteps1') was never finished, but helped me wrap my head around how I was going to calculate all of ")
   print(" the possible combinations of 1 and 2 steps to reach n. It created a list of length n containing only 1s, then ")
   print(" checked if the n was even to see if it would be possible to replace every 1 in the list with a 2 without leftovers.")
   print(" Once I started trying to figure out the mix of 1 and 2, as well as trying n=3, I decided I was going to have to change")
   print(" how it worked. ")
   print("-" * 50)
   print("\n 'calcSteps2' was different, I managed to get it to output the correct number from the examples, but when increasing n, ")
   print(" I realized the logic was not working correctly. I believe this is due to how I was adding 2s and deleting 1s from")
   print(" the lists, as well as how it handled an n that was an odd number that needed a single 1 to be kept in the list. ")
   print(" I was in a rush when I wrote it, and besides not working right, it was in need of a pretty good clean up too, so...")
   print("-" * 50)
   print("\n I re-worked into 'calcSteps', and split it into 3 additional functions: \n 'put2InList', 'validateSumAndFindPermutations' and 'savePermutations'")
   print("\n CalcSteps is solid mix of the first 2 versions, but it actually works as expected with an n up to 11, or 14 if")
   print(" you don't mind waiting about 6 mins for it to calculate all 610 possible permutations. And 13 only took")
   print(" about 1 minute to find 377 possible orders, so clearly increasing n expontentially increases the amount of distinct")
   print(" and possible ways of 'climbing to the top of the stairs', and drastically increases the run time of the program.")
   print("-" * 50)
   print("\n It works by creating a list of length n full of 1s, then checking if n is even or odd. If even, it then loops")
   print(" through the list of 1s (n/2) times, each time replacing the first 2 1s in the list with a 2, until the list")
   print(" IS ALL 2s! If it is odd, it does the same but ( (n-1) / 2)) times instead, since it can only replace a pair")
   print(" of 1s with a 2 and needs to leave a single 1 alone. Each run of the loop sends the original list to 'put2InList',")
   print(" and it gets sent back the new version of the list containg one 2 in the place of two 1s. \n")
   print(" Then it sends that new list to 'validateSumAndFindPermutations', where the sum of the list is checked against n.")
   print(" If it is equal to n, that means that the list is valid, if it is equal to (n-1), then we know that we need to")
   print(" add a single 1 to the list to correct it (it must of been an odd n). It then checks how many items are in the list,")
   print(" and if there is only one (in the case of n=2), then it just sends the list back to calcSteps right there since there")
   print(" is no other possible permutations to calculate. If there is more than one item however, it then uses .permutations() ")
   print(" and sets in order to calculate a list containting all the other possible orders of steps using that list, and ")
   print(" then finally it sends that big list back to calcSteps.\n")
   print(" Lastly, calcSteps then sends its version of fullStepsList and the permutations list that it received to ")
   print(" 'savePermutations'. Here the length of the list of permutations is checked to see if there is more than one, or")
   print(" only 1, and then it sends the permutations of that current loop to the main calcSteps fullStepsList, so that by the")
   print(" time all the permutations are found, calcSteps can just return the amount of permutations in the fullStepsList.")
   print("-" * 50)
   print(" I also have checks for an n that is equal to or less than 0, and I did have a test for a string, but its commented")
   print(" out because it fully stops the program from running at all. ")
   print("-" * 50)
   print(" Overall I'm pretty happy with it in its current state and think I accomplished what the exercise was going for,")
   print(" and while it seemed like it was going to be quite simple at the start, I'm glad that it turned out to be a bit")
   print(" more involved than anticipated. I'm also positive that there are other ways to do it, and I'm confident in my ")
   print(" version, but I do think there might be more efficient ways to do it hypothetically.  ")

if __name__ == "__main__":
   main()
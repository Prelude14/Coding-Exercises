""" Single Number Exercise:

   Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

   You must implement a solution with a linear runtime complexity and use only constant extra space.*****************************

   Example 1:
   Input: nums = [2,2,1]
   Output: 1

   Example 2:
   Input: nums = [4,1,2,1,2]
   Output: 4

   Example 3:
   Input: nums = [1]
   Output: 1

"""
#So linear complexity means we can use at most one for loop at a time to check the array's elements, and then only constant extra space means we can't use any variables that would scale with 
#the size of the original array, i.e. no nested loops (= O(n^2) != O(n)), and no new list to store vals from the original list, we can only use variables with O(1) space like ints or bools...

def findSingleNum(nums: list[int]):

   result = nums[0] #need to assign result to equal first val in list before the for loop runs, in order to compare it to every other value
   
   #so we are going to use a bitwise XOR (or Exclusive Or, using "^") in order to find out if the current value is a duplicate or not. It is going to compare the bits of two ints, and return
   #a NEW BINARY number made up of xor-ing each bit in each integer (5^3 == 101^011 in Binary, 1^0=1, 0^1=1, 1^1=0, so it returns the binary 110, which is equal to int 6)
   #if 2 bits are equal it returns 0 in that place, and if they are different, it returns a 1 in that place

   print(f" First result value (nums[0]): {result} ")

   for i in range(1,len(nums)): #need to check every value in nums starting with second since result starts as the first val

      print(f"\n Result before XOR: {result}, Nums[{i}]: {nums[i]}")
      print(f"\n Result Binary before: {bin(result)}, Nums[{i}] Binary: {bin(nums[i])}")
      result ^= nums[i] #result is equal to the previous result XOR-ed against current val at num[i], when new int is found, its binary is essentially added to result, and when duplicate is found
      #its binary is subtracted, so when for loop ends we are left with the binary of the int that was never subtracted, giving us the int in nums that only appears once. 
      print(f"\n Result after XOR: {result}, Result Binary after: {bin(result)}, =========================================End of each FOR loop")
      
   return result

def main():
   print("=" * 50)
   print(" Single Number EXERCISE")
   print("=" * 50)

   #=========================================================== NUMS 1 ========================================
   nums1 = [2,2,1]

   print("\n Input nums 1: ") #print nums1 to console,
   print(nums1)
   print("-" * 50)

   print("\n Output 1:") 
   print("-" * 50)
   print("\n Single Num1: ", findSingleNum(nums1)) 
   print("=" * 50)

   #=========================================================== NUMS 2 ========================================
   nums2 = [4,1,2,1,2]

   print("\n Input nums 2: ") #print nums2 to console,
   print(nums2)
   print("-" * 50)

   print("\n Output 2:") 
   print("-" * 50)
   print("\n Single Num2: ", findSingleNum(nums2)) 
   print("=" * 50)

   #=========================================================== NUMS 3 ========================================
   nums3 = [1]

   print("\n Input nums 3: ") #print nums3 to console,
   print(nums3)
   print("-" * 50)

   print("\n Output 3:") 
   print("-" * 50)
   print("\n Single Num3: ", findSingleNum(nums3)) 
   print("=" * 50)


if __name__ == "__main__":
   main()
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
   
   for index, val in enumerate(nums):

      
      


def main():
   print("=" * 50)
   print(" Single Number EXERCISE")
   print("=" * 50)

   #=========================================================== NUMS 1 ========================================
   nums1 = [2,2,1]

   print("\n Input nums 1: ") #print nums1 to console,
   print(nums1)
   print("-" * 50)

   print("\n Output:") 
   print("-" * 50)
   print("\n", findSingleNum(nums1)) 


   """
   #=========================================================== NUMS 2 ========================================
   nums2 = [4,1,2,1,2]

   print("\n Input nums 2: ") #print nums2 to console,
   print(nums2)
   print("-" * 50)

   print("\n Output:") 
   print("-" * 50)
   print("\n", findSingleNum(nums2)) 

   #=========================================================== NUMS 3 ========================================
   nums3 = [1]

   print("\n Input nums 3: ") #print nums3 to console,
   print(nums3)
   print("-" * 50)

   print("\n Output:") 
   print("-" * 50)
   print("\n", findSingleNum(nums3)) 
   """
if __name__ == "__main__":
   main()
class Solution(object): # Define a class named Solution
    def maxAdjacentDistance(self, nums):# Define a method inside the class that takes a list `nums`
      n = len(nums)# Store the length of the list in variable `n`
      res =  float("-inf")# Initialize result with negative infinity
        # print(res)
      for i in range(1, n): # Loop from index 1 to n-1
        if i == n-1: # If we are at the last element of the list
                diff = abs(nums[-1] - nums[0])# Difference between last and first element
                res = max(res, diff) # Update the result if this difference is larger
                # print("last: ",diff)
        diff = abs(nums[i-1] - nums[i])# Difference between current and previous elemen
                # print("loop: ",diff)
        res = max(res, diff) # Update max result if this difference is larger
        
        # print(res)
      return res# Finally, return the largest adjacent difference found

      '''If nums = [5, 2, 9, 4]:

Differences:
|5 - 2| = 3
|2 - 9| = 7
|9 - 4| = 5
|4 - 5| = 1 ← last and first

Maximum = 7

'''


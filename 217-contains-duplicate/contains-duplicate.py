class Solution(object):
    def containsDuplicate(self, nums):
        seen = set() #creates an empty set to keep track of unique numbers.
        for num in nums: #For each num in the list:
            if num in seen: #If num is already in seen, it means it’s a duplicate → return True.
                return True
            seen.add(num)#Otherwise, add num to the set.
        return False

''' Use a Set (Best approach)--> 
Create an empty set.

Loop through each number.

If it already exists in the set → return True.

If loop completes → return False.

Time Complexity: O(n)'''
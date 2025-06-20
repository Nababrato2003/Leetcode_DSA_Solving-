class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []  # This will store the final result

        # Loop over each element in nums by index
        for i in range(len(nums)):
            count = 0  # Count how many numbers are smaller than nums[i]

            # Compare nums[i] with every other number in the array
            for j in range(len(nums)):
                # Skip comparing the number with itself
                if i != j and nums[j] < nums[i]:
                    count += 1  # Found a smaller number

            # After checking all elements, store the count in result
            result.append(count)

        return result  # Return the final result array

        ## BRUTE FORCE USED HERE 

'''For nums = [8, 1, 2]:

i = 0 → nums[0] = 8
→ Compare with 1 and 2 → Both < 8 → count = 2

i = 1 → nums[1] = 1
→ Compare with 8 and 2 → None < 1 → count = 0

i = 2 → nums[2] = 2
→ Compare with 8 and 1 → Only 1 < 2 → count = 1

Result = [2, 0, 1]'''

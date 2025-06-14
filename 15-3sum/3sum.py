class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Step 1: Sort the array
        res = []     # To store the final result

        for i in range(len(nums)):
            # Step 2: Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Two-pointer setup
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Step 4: Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1  # Increase sum by moving left pointer
                else:
                    right -= 1  # Decrease sum by moving right pointer

        return res

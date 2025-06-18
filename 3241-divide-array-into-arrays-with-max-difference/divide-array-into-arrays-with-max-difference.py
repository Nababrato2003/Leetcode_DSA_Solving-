class Solution(object):
    def divideArray(self, nums, k):
        n = len(nums)
        if n % 3 != 0:
            return []

        nums.sort()
        result = []

        for i in range(0, n, 3):
            group = nums[i:i+3]
            if group[2] - group[0] > k:
                return []
            result.append(group)

        return result
       
        
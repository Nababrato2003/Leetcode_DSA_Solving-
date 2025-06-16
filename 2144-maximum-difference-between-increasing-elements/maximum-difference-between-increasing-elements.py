class Solution(object):
    def maximumDifference(self, nums):
        min_ = nums[0]
        res = 0
        for n in nums:
            min_ = min(n, min_)
            res = max(res, n - min_)
        return res if res > 0 else -1
       
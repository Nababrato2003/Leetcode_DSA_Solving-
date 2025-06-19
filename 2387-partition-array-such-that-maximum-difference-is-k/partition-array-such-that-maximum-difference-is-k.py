class Solution(object):
    def partitionArray(self, nums, k):
        res = 1
        nums.sort()

        l = 0
        for r in range(len(nums)):
            if nums[r]-nums[l]>k:
                res += 1
                l = r
    
        return res
       
        
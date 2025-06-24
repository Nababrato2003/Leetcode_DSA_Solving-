class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = set()
        
        for j in range(n):
            if nums[j] == key:
                
                for i in range(max(0, j - k), min(n, j + k + 1)):
                    result.add(i)
        
        return sorted(result)

        
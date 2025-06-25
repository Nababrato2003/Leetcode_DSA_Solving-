class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        def leq(x):
            count = 0
            for i in nums1:
                if i > 0:
                    count += bisect.bisect_right(nums2, x // i)
                elif i < 0:
                    count += len(nums2) - bisect.bisect_left(nums2, -(-x // i))
                else:  
                    if x >= 0:
                        count += len(nums2)
            return count

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1        
        left, right = -10 ** 10, 10 ** 10         
        while left < right: 
            mid = (left + right) // 2

            if leq(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
class Solution(object):
    def minimizeMax(self, nums, p):
        nums.sort()
        n=len(nums)
        def check_pairs(arr,target):
            pairs=0
            i=0
            n=len(arr)
            while i+1<n:
                if arr[i+1]-arr[i]<=target:
                    pairs+=1
                    i+=2
                else:
                    i+=1
            return pairs
        min_diff=0
        max_diff=nums[-1]-nums[0]
        left=min_diff
        right=max_diff
        while left<right:
            mid=(left+right)//2
            if check_pairs(nums,mid)>=p:
                right=mid
            else:
                left=mid+1
        return left
    

    """
This is how I made sense of the question:
Sort the list.
Guess the minimum maximum difference.
Count how many pairs in nums have a difference equal to or less than this guess.
If the count is too high (more than or equal to p) then guess a lower value.
Otherwise, guess a higher value.
The smallest guess will be 0 and the highest guess will be nums[numsSize-1] - nums[0] (assuming nums is sorted).
The answer will be the smallest guess that gives a pair count equal to p
"""
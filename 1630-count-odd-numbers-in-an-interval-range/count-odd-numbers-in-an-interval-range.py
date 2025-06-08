class Solution(object):
    def countOdds(self, low, high):
       a = (high+1)//2 - (low//2)
       return a
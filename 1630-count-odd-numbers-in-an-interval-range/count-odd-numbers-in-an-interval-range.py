class Solution(object):
    def countOdds(self, low, high):
       a = (high+1)//2 - (low//2)
       return a

       '''(high + 1) // 2 - (low // 2)
       Counts how many odd numbers are in the range [low, high].'''

       
       '''(7 + 1) // 2 - (3 // 2)
        = 8 // 2 - 1
        = 4 - 1 = 3 ✅'''

class Solution(object):
    def maxDifference(self, s):
         q = Counter(s).values()
         return max(v%2*v for v in q)-min(v for v in q if v%2^1)
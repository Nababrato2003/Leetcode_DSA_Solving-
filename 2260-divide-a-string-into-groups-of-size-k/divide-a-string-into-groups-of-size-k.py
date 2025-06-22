class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        rel = []
        i = 0
        while i < len(s):
            rel.append(s[i: i+k])
            i += k

        if len(rel[-1]) < k:
            rel[-1] = rel[-1] + fill*(k - len(rel[-1]))
        return rel
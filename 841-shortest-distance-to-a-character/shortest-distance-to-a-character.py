class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        ans = [10**5] * n
        prev = -10**5
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev
        prev = 10**5
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans
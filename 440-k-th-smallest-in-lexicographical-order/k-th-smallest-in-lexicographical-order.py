class Solution:
    def findKthNumber(self, n, k):
        def count_prefix(prefix, n):
            count = 0
            curr = prefix
            next_prefix = prefix + 1
            while curr <= n:
                count += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return count

        curr = 1
        k -= 1  # '1' is the first number in lex order

        while k > 0:
            count = count_prefix(curr, n)
            if count <= k:
                k -= count
                curr += 1
            else:
                k -= 1
                curr *= 10

        return curr
import heapq

class Solution:
    def clearStars(self, s):  # Removed ": str"
        minH = []  # min-heap to store (char, -index)
        s = list(s)  # convert string to list for in-place editing

        for i in range(len(s)):
            ch = s[i]
            if ch == "*" and minH:
                del_char, j = heapq.heappop(minH)
                s[i] = ""         # remove current '*'
                s[-j] = ""        # remove corresponding character using -index
            else:
                heapq.heappush(minH, (ch, -i))  # store character and negative index
        
        return "".join(s)  # Removed "-> str"

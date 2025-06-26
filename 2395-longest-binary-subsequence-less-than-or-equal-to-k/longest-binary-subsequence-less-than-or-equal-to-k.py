class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == '' or k == 0:
            return 0
        elif s == '0':
            return 1
        
        bin_k = bin(k)[2:]
        k_len = len(bin_k)
        if k_len >= len(s):
            return len(s)
        zeros_count = 0
        for i in range(0,len(s)-k_len):
            if s[i] == '0':
                zeros_count += 1
        
        pow2 = 1
        value = 0
        count = 0
        
        if int(s[-k_len:],2) > k:
            for i in range(len(s)-1,-k_len - 1,-1):
                if s[i] == '0':
                    count +=1
                else:
                    if pow2 <= k:
                        value += pow2
                        if value < k:
                            count += 1
                        else:
                            break
                        
                pow2 *= 2
            return zeros_count + count
        return zeros_count + k_len
        
        
        
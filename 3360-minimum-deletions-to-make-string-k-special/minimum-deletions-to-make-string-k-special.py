class Solution(object):
    def minimumDeletions(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        wordDict = {}

        for i in word:
            if i in wordDict:
                wordDict[i]+=1
            else:
                wordDict[i]=1
        
        freq_list=[]

        for i in wordDict.values():
            freq_list.append(i)
        freq_list.sort()

        res=float('inf')

        for base in freq_list:
            deletion=0
            for f in freq_list:
                if f < base:
                    deletion+=f
                elif f>base+k:
                    deletion+=f-(base+k)
            if deletion<res:
                res=deletion
        
        return res
        
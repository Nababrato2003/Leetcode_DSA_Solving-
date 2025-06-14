class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=str(num)
        n=len(num)
        i=0
        while i<n-1 and num[i]=="9":
            i+=1
        return int(num.replace(num[i],"9"))-int(num.replace(num[0],"0"))
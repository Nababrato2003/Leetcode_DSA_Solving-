class Solution(object):
    def lexicalOrder(self, n):
        output=[]
        if n<10:
            for i in range(1,n+1):
                output.append(i)
            return output
        
        for i in range(1,n+1):
            x=str(i)
            output.append(x)
        output=sorted(output)
        ans=[]
        for o in output:
            z=int(o)
            ans.append(z)
        return ans
        
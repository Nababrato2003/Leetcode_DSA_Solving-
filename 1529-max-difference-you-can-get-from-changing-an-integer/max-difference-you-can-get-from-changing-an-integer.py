class Solution(object):
    def maxDiff(self, num):
        number = str(num)
        maxi = number
        mini = number
        
        for i in number:
            if i != '9':
                maxi = number.replace(i, '9')
                break
        
        if number[0] != '1':
            mini = number.replace(number[0], '1')
        else:
            for i in number[1:]:
                if i != '0' and i != number[0]:
                    mini = number.replace(i, '0')
                    break

        return int(maxi) - int(mini)
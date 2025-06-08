class Solution(object):
    def fizzBuzz(self, n):
        ans = [] #ans will store all the answers ("Fizz", "Buzz", numbers, etc.)


        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                    ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans
        
    '''| i | Condition     | What is appended | ans list                          |
| - | ------------- | ---------------- | --------------------------------- |
| 1 | not divisible | `"1"`            | `["1"]`                           |
| 2 | not divisible | `"2"`            | `["1", "2"]`                      |
| 3 | i % 3 == 0    | `"Fizz"`         | `["1", "2", "Fizz"]`              |
| 4 | not divisible | `"4"`            | `["1", "2", "Fizz", "4"]`         |
| 5 | i % 5 == 0    | `"Buzz"`         | `["1", "2", "Fizz", "4", "Buzz"]` |
'''
        
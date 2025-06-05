class Solution(object):
    def maxArea(self, height):
      
        max_area = 0
        left = 0
        right = len(height)-1

        while left < right:
            
            h = min(height[left],height[right])
            w = right - left
            area = h * w

            max_area = max(area,max_area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_area 
        

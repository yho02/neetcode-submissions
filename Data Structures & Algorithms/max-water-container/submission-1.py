class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tmp = 0
        max = 0 
        left, right = 0, len(heights) - 1
        while left < right:
            tmp = min(heights[left], heights[right]) * (right - left)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
            if tmp > max:
                max = tmp
        return max